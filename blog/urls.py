from django.urls import path
from blog import views

urlpatterns = [
    path('about', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:post_id>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:post_id>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:post_id>/remove', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/drafts', views.DraftListView.as_view(), name='draft_list'),
    path('post/<int:post_id>/comment', views.comment_add_to_post, name='comment_add_to_post'),
    path('comment/<int:comment_id>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<int:comment_id>/remove', views.comment_remove, name='comment_remove'),
    path('post/<int:post_id>/publish', views.post_publish, name='post_publish'),
]