from django.shortcuts import render
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-date')[:5]
    
    return render(request,'blog/home.html',{'blogs':blogs})

