from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="home"),
    path('about/', views.about ,name="about"),
    path('detail/<int:post_id>/', views.post_detail ,name="detail"),
    path('newPost/', views.PostCreateView.as_view(),name="newPost"),
    path('detail/<slug:pk>/update/', views.PostUpdateView.as_view() ,name="post_update"),
    path('detail/<slug:pk>/delet/', views.PostDeleteView.as_view() ,name="post_delet"),


]