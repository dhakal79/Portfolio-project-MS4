from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm

#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post_page.html'
    #fields = '__all__'      

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
    #fields = ['title', 'slug', 'content']
