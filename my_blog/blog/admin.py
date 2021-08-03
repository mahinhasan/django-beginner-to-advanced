from django.contrib import admin
from .models import *
from . import models
# Register your models here.
class CommentInLine(admin.TabularInline):
    model = models.Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)

