from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts_list'
    model = Post

    def get_queryset(self):
        return Post.objects.all
