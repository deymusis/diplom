from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('reg/', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('create-link/', userViews.link, name='links'),
    path('link/<slug>/', userViews.redirect_url_view, name="redirect-link")
]
