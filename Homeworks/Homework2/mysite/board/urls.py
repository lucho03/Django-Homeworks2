from django.urls import URLPattern
from django.urls.conf import path
from board import views

urlpatterns = [
    path('departure board', views.show),
    path('', views.show),
]