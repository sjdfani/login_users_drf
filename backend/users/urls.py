from django.urls import path
from .views import LoginUser

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser.as_view()),
]
