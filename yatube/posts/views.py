from turtle import title
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post, Group

# Create your views here.
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
               'posts': posts,
    }
    return render(request, template, context)
#    return HttpResponse('Главная страница')

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('pub_date')[:10]
    template = 'posts/group_list.html'
    context = {
               'group': group,
               'posts': posts,
    }
    return render(request, template, context)
#    return HttpResponse(f'Список сообществ {slug}')