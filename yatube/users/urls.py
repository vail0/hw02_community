# users/urls.py

from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
      'logout/',
      # Прямо в описании обработчика укажем шаблон, 
      # который должен применяться для отображения возвращаемой страницы.
      LogoutView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
]