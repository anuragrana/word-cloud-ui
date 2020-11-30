from django.urls import path

from . import views

app_name = "word_cloud_app"
urlpatterns = [
    path(r'', views.home, name='home'),
]
