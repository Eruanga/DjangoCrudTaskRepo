from django.urls import path
from blog.views import blog
from .views import PostCreateView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
	path("blog/", include("blog.urls", namespace="blog")),
	path('', PostListView as_view(), name='post'),
	path('post/<str:pk>/'. PostDetailView as_view(), name='post'),
	path('post-create/'. PostCreateView as_view(), name='post-create'),
	path('post-update/<str:pk>/'. PostUpdateView as_view(), name='post-update'),
	path('post-delete/<str:pk>/'. PostDeleteView as_view(), name='post-delete'),
]