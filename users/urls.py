from django.urls import path, URLPattern
from users import views

app_name = 'user'
urlpatterns: list[URLPattern] = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
]
