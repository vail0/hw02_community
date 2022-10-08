# users/urls.py

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        # Прямо в описании обработчика укажем шаблон,
        # который должен применяться для отображения возвращаемой страницы.
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'signup/',
        views.SignUp.as_view(),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
  
    # Смена пароля
    path(
        'password_change/',
        views.PasswordChangeView.as_view(),
        name='password_change'
    ),

    # Сообщение об успешном изменении пароля
    path(
        'password_change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    # Восстановление пароля
    path(
        'password_reset/',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),

    # Сообщение об отправке ссылки для восстановления пароля
    path(
        'password_reset/done/',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

    # Вход по ссылке для восстановления пароля
    path(
        'reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
        ),

    # Сообщение об успешном восстановлении пароля
    path('reset/done/',
    views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete'
    ),
]
