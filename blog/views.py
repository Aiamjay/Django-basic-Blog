from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Post
from blog.forms import PostForm


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts_list'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published=True)


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm


class DetailPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = '/login/'
    form_class = PostForm
    template_name = 'blog/post_create.html'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/post_delete.html'
    context_object_name = 'object'


class DraftsListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'list'
    template_name = 'blog/drafts_list.html'
    user = None

    def get_queryset(self):
        return Post.objects.filter(author=self.user.pk).filter(published=False)

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(DraftsListView, self).dispatch(request, *args, **kwargs)


class AllWorksListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'list'
    template_name = 'blog/drafts_list.html'
    user = None

    def get_queryset(self):
        return Post.objects.filter(author=self.user.pk)

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(AllWorksListView, self).dispatch(request, *args, **kwargs)


@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_list')
