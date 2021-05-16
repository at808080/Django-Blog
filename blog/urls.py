from django.urls import path
from . import views
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-home'),#path('', views.home, name='blog-home'),
    path('blogpost/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'), #django automatically passes the id in the url to the class based view
    path('blogpost/create/', BlogPostCreateView.as_view(), name='blogpost-create'),
    path('blogpost/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost-update'), 
    path('blogpost/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost-delete'), 
    path('about/', views.about, name='blog-about')

]
