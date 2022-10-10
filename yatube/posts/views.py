from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()
    paginator = Paginator(posts, settings.AMOUNT)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)
    paginator = Paginator(posts, settings.AMOUNT)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)

    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    author = get_object_or_404(User, username=username)
    posts_auth = author.posts.all()

    paginator = Paginator(posts_auth, 10)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'posts_auth': posts_auth,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = get_object_or_404(Post, pk=post_id)
    posts_by = post.author.posts.all()
    context = {
        'post': post,
        'posts_by': posts_by,

    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    # Проверяем, получен POST-запрос или какой-то другой
    if request.method == "POST":
        # Создаём объект формы класса ContactForm
        # и передаём в него полученные данные
        form = PostForm(request.POST)
        if form.is_valid():

            # Берём валидированные данные формы из словаря form.cleaned_data
            # text = form.cleaned_data['text']
            # group = form.cleaned_data['group']

            form.author = request.user
            form.save()

            return redirect("posts:profile", request.user)
        return render(request, "posts/create_post.html", {'form': form})
    # Если пришёл не POST-запрос - создаём и передаём в шаблон пустую форму
    # пусть пользователь напишет что-нибудь
    form = PostForm()
    return render(request, "posts/create_post.html", {'form': form})


def post_edit(request):

    pass
