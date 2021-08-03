from django.shortcuts import render
from django.views.generic import ListView,TemplateView,CreateView,UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePageView(ListView):

    """Django ListView return a object called 'object_list' """

    model = Post
    template_name = 'blog/index.html'
class PostDetailView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'postDetail'
    login_url = 'login'

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','body']
    template_name = 'blog/create_post.html'

    success_url  = reverse_lazy('home')
    login_url = 'login'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','body']
    template_name = 'blog/edit_post.html'
    login_url = 'login'

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
    login_url = 'login'