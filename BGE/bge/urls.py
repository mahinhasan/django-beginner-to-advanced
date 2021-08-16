from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('create',views.CreatePost.as_view(),name='create'),
    path('detail/<int:pk>',views.DetailPage.as_view(),name='detail'),
    path('update/<int:pk>/',views.EditPage.as_view(),name='update'),
    path('delete/<int:pk>/',views.DeletePostView.as_view(),name='delete')
]
