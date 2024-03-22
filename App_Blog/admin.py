from django.contrib import admin
from App_Blog.models import Blog, Comment, Likes

# Register your models here.
models_to_register = [Blog, Comment, Likes]

for model in models_to_register:
    admin.site.register(model)