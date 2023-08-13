from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'chat'

urlpatterns = [
    path("", index, name="index"),
    path("chat/<str:room_name>/", room, name="room"),
    path("create_group/", create_group, name="create_group"),
    path("register/", register_user, name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
