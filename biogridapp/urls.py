from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),     
    path('add/',views.add_bio,name='bio_add'),
    path('delete/<int:id>/', views.delete_bio, name='bio_delete'),          
]