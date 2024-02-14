from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('post/<str:var>/', views.post, name='post'),
    path('post_links/', views.post_links, name='post_links')
]