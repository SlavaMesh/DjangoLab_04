from django.shortcuts import render
from django.db import models
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    model = Post
    ordering = '-date'
    template_name = '../templates/flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SearchList(ListView):
    model = Post
    ordering = '-date'
    template_name = '../templates/flatpages/search.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = '../templates/flatpages/post.html'
    context_object_name = 'post'


class ADD(CreateView):
    template_name = '../templates/flatpages/add.html'
    form_class = PostForm


class Update(UpdateView):
    template_name = '../templates/flatpages/add.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class Delete(DeleteView):
    template_name = '../templates/flatpages/delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'