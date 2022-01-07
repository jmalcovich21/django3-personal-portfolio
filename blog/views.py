from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # blogs = Blog.objects.all() - cargar todos los objetos de la clase Blog
    blogs = Blog.objects.order_by('-date') # ordena por fecha del mas actualizado, solo los ultimos 3 con slicing
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
