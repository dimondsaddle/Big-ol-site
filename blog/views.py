from django.shortcuts import render , get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs =Blog.objects.order_by("-date")[:5]
    every_blog = Blog.objects.all()
    return render(request, "blog/all_blogs.html",{"blogs":blogs,"every_blog":every_blog})

def detail(request, blog_id):
    blog =get_object_or_404(Blog, pk=blog_id)
    return render(request,"blog/detail.html",{"blog":blog})
