from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Define a view for the root path "/"
    path('', views.videos, name='videos'),  # Define '/videos/' route
]
