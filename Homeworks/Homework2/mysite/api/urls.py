from django.urls import path
from django.urls.resolvers import URLPattern
from api import views

urlpatterns = [
    path('api', views.get_json),
]