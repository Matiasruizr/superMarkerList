"""superMarkerList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from superMarkerList import views
from perfiles.views import SignUpView
from perfiles.views import SignInView
from perfiles.views import SignOutView,BienvenidaView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy



urlpatterns = [
     # Todas las url de productos
    path('producto/', include('producto.urls')),
    path('admin/', admin.site.urls),
    path('', views.inicio, name='home'),
    path('bienvenido/', BienvenidaView.as_view(), name='bienvenida'), 
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('iniciar-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),

     path(
        'password/recovery/',
        auth_views.PasswordResetView.as_view(
            template_name='auth/password_reset_form.html',
            html_email_template_name='auth/password_reset_email.html',
        ),
        name='password_reset',
    ),

    path(
        'password/recovery/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html',
        ),
        name='password_reset_done',
    ),

    path(
        'password/recovery/     ',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('home'),
            post_reset_login=True,
            template_name='auth/password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),

    path(
        'password_update/',
        auth_views.PasswordChangeView.as_view,
        {
            'template_name': 'auth/password_change_form.html',
            'post_change_redirect': 'auth_password_change_done',
        },
        name='auth_password_change',
    ),

    path(
        'password_update_done/',
        auth_views.PasswordChangeDoneView.as_view,
        {
            'template_name': 'auth/password_change_done.html',
        },
        name='auth_password_change_done',
    ),

]
