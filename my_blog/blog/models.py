from django.db import models
from django.urls import reverse
from my_blog import settings

class Post(models.Model):
    title = models.CharField(max_length=250)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    body = models.TextField()

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    


    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    