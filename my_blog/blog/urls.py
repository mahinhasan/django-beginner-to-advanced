from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('create',views.CreatePostView.as_view(),name='create_post'),
    path('post/<int:pk>/detail',views.PostDetailView.as_view(),name='detail'),
    path('post/<int:pk>/edit/',views.UpdatePostView.as_view(),name='edit'),
    path('post/<int:pk>/delete/',views.DeletePostView.as_view(),name='delete')
]
