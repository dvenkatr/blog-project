from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.contrib.auth import views

from django.views.generic import (TemplateView, 
                                    CreateView, UpdateView, DeleteView,
                                    ListView, DetailView)

from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.utils import timezone

"""
Posts
"""

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        # Field lookups
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'next'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish
    return redirect('post_detail', pk=post.pk)

"""
Comments
"""

@login_required
def comment_add_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm
        return render(request, 'blog/comment_form.html', {'form' : form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve() # From models
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)





