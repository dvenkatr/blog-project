from django.urls import path
from blog import views

urlpatterns = [
    path('about', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:post_id>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:post_id>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:post_id>/remove', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/drafts', views.DraftListView.as_view(), name='draft_list'),
]