from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'home.html'
    ordering = ['-id']
    paginated_by = 6
   

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post_page.html'
    #fields = '__all__'      

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'  
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')    


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category_page.html'
    fields = '__all__'    


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
    #fields = ['title', 'slug', 'content']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    