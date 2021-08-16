from django.shortcuts import redirect, render
from .models import *
from .form import *
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,CreateView,DetailView

# Create your views here.


class HomePage(ListView):
    model = Bge
    ordering = '-time'
    template_name = 'bge/index.html'


class CreatePost(CreateView):
    model = Bge

    def get(self, request):
        form = PostForm()
        return render(request, 'bge/create_post.html', {'form':form})
    def post(self, request):
        if request.method == 'POST':
            
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                body = form.cleaned_data['body']

                add_post = Bge.objects.create(title=title, body=body)
                add_post.save()
                form = PostForm()
                return redirect('home')

            return render(request,'bge/create_post.html',{'form':form})



class DetailPage(DetailView):
    model = Bge
    template_name='bge/detail.html'
    context_object_name = 'detailview'


class EditPage(UpdateView):
    model = Bge
    fields = ['title','body']
    template_name = 'bge/update_post.html'

class DeletePostView( DeleteView):
    model = Bge
    template_name = 'bge/delete_post.html'
    success_url = reverse_lazy('home')
    