from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.project_details, name='project_details'),
    re_path(r'^about/', views.about, name='about'),
]
