import hashlib
import os
import sys
from io import BytesIO

from django import forms
from django.conf import settings
from django.core.cache import cache
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import path
from django.views.decorators.http import etag
from PIL import Image, ImageDraw
from django.urls import reverse
from django.shortcuts import render
from pathlib import Path


DEBUG = os.environ.get("DEBUG", 'on') == 'on'
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')


BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

# settings
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    # INSTALLED_APPS=(
    #     'django.contrib.staticfiles',
    # ),
    # TEMPLATE_DIRS=(
    #     os.path.join(BASE_DIR, 'templates'),
    # ),
    # STATICFILES_DIRS=(
    #     os.path.join(BASE_DIR, 'static'),
    # ),
    # STATIC_URL='/static/',
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),


    MIDDLEWARE=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ),


    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
        },
    ),

    STATIC_URL='/static/',
    STATICFILES_DIRS=[(os.path.join(BASE_DIR,'static'))]

)


# forms that validated the user input
class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""

    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        """Generate an image of the given type and return as raw bytes."""
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']

        key = '{}.{}.{}'.format(width, height, image_format)
        content = cache.get(key)
        if content is None:
            image = Image.new('RGBA', (width, height), color='blue')
            draw = ImageDraw.Draw(image)
            text = '{} X {}'.format(width, height)
            textwidth, textheight = draw.textsize(text)
            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft, texttop), text, fill=(255, 255, 255))
            content = BytesIO()
            # image.save(raw bytes,image_format) # raw bytes are optional here
            image.save(content, image_format)
            content.seek(0)  # move to the beginning of file after writing
            cache.set(key, content, 60*60)  # cached for 60s
        return content


# views


def generate_etag(request, width, height):
    content = 'Placeholder: {} x {}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


@etag(generate_etag)
def placeholder(request, width, height):
    # ImageForm(dict) return ImageForm Object
    form = ImageForm({'width': width, 'height': height})

    # check form is valid or not
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest("Invalid Response.")


def index(request):
    example = reverse('placeholder', kwargs={'width': 50, 'height':50})
    
    context = {
        # 'example': request.build_absolute_uri(example)
        'example': 'this',
        'c':c,
    }

    return render(request, 'index.html', context)


# url
urlpatterns = [
    path('', index, name='index'),
    path('images/<int:width>x<int:height>/', placeholder, name='placeholder'),
    # path('images/<int:width>/<int:height>/', placeholder, name='placeholder'),
]

application = get_wsgi_application()

# manage.py
if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)