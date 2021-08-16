from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Bge(models.Model):
    title = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    body = RichTextUploadingField()



    def __str__(self):
        return self.title[:40]

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk': self.pk})
