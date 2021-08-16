from django import forms
from django.forms import fields
from .models import *
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(),required=True, max_length=300)
    body = RichTextField()

    class Meta:
        model = Bge
        fields = ('title','body')