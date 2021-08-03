
from django.contrib import admin, auth
from django.urls import path,include
from django.views.generic.base import TemplateView
urlpatterns = [
    path('login', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')), # django built in authentication 
    path('user/',include('account.urls')),
    path('',include('blog.urls')),
]
