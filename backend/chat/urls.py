from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [
    path("", index, name="index"),
    path("chat/<str:room_name>/", room, name="room"),
    path("create_group/", create_group, name="create_group"),
    path("register/", register_user, name="register"),
]