from django.urls import path
from . import views

from . import views
# from django.contrib import admin

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
    # The 'user/<str:username>/' URL pattern captures a username as a string and passes it to the UserPostListView.
    # This allows the view to filter posts by the specified user.
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
   
    path('about/', views.about, name='blog-about'),
]
#<app>/<model>_<viewtype>.html
#<blog>/<post>_<list>.html