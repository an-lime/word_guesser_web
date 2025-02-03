from django.urls import path, include, URLResolver

urlpatterns: list[URLResolver] = [
    path('', include('main.urls', namespace='main')),
    path('user/', include('users.urls', namespace='user')),
]
