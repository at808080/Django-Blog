from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

#class based views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

posts = [
    {
        'author': 'User1',
        'title': 'Post 1',
        'content': 'First post content...',
        'date_posted': '4/5/2021'
    },
    {
        'author': 'User1',
        'title': 'Post 1',
        'content': 'First post content...',
        'date_posted': '4/5/2021'
    },
    {
        'author': 'User1',
        'title': 'Post 1',
        'content': 'First post content...',
        'date_posted': '4/5/2021'
    }
]


def home(request):
    context = {
        'title': 'Home Page',
        'posts': BlogPost.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About Page',
    }
    return render(request, 'blog/about.html', context)

#class based views
#more built in functionality handling backend

class BlogPostListView(ListView):
    model = BlogPost 
    template_name = 'blog/home.html' #assign the template for the view to render
    context_object_name = 'posts'
    ordering = ['-date_added']

class BlogPostDetailView(DetailView):
    model = BlogPost 
    #template_name = 'blog/blogpost-detail.html' #assign the template for the view to render

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author of the new blog post in the form to the current logged in user
        return super().form_valid(form) # validate the form as per usual using the super class CreateView's form_valid function

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author of the new blog post in the form to the current logged in user
        return super().form_valid(form) # validate the form as per usual using the super class CreateView's form_valid function

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost 
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

