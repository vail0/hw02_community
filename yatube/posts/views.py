from django.shortcuts import get_object_or_404, render
from .models import Post, Group
from django.conf import settings


# Create your views here.
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:settings.AMOUNT]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:settings.AMOUNT]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
