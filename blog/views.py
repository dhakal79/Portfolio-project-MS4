from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

# def home(request):
#   return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home.html"
    ordering = ["-id"]
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__icontains=cats.replace("-", " "))
    cat_menu = Category.objects.all()
    paginate_by = 6
    return render(
        request,
        "categories.html",
        {"cats": cats.title().replace("-", " "), "category_posts": category_posts, "cat_menu": cat_menu},
    )
    

class ArticleDetailView(DetailView):
    model = Post
    template_name = "post_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post_page.html"
    # fields = '__all__'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    success_url = reverse_lazy("home")


class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category_page.html"
    fields = "__all__"
   

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "edit_post.html"
    # fields = ['title', 'slug', 'content']

   # def post(self, request, *args, **kwargs):
    #    print(request)
    #    print(request.user.username)
    #    form = self.form_class(request.POST)
    #    return render(request, self.template_name, {"form": form})


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_details", args=[slug]))
