from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<topic_name>/", views.forum, name="forum"),
]