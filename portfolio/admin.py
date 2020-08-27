from django.contrib import admin
from .models import Project
from blog.models import Blog
admin.site.register(Blog)

admin.site.register(Project)
# Register your models here.
