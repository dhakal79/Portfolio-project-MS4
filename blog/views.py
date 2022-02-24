from django.shortcuts import render, get_object_or_404, reverse, redirect

from django.contrib.messages.views import SuccessMessageMixin
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
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


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

class CategoryView(ListView):
    model = Category
    template_name = "categories.html"
    ordering = ["-id"]
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        category_slug = self.kwargs["cats"]
        context["cats"] = category_slug
        articles = Post.objects.filter(
            category__icontains=category_slug.replace("-", " ")
        )
        paginator = Paginator(articles, self.paginate_by)

        page = self.request.GET.get("page")

        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        context["article_list"] = articles
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = "post_details.html"

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            cat_menu = Category.objects.all()
            number_of_likes = post.number_of_likes()
            data = {
                'cat_menu': cat_menu,
                'number_of_likes': number_of_likes,
                'user': self.request.user,
                'post': post,
                }
        except Post.DoesNotExist:
            return redirect('/404')
        except:
            return redirect('/500')
        return render(request, 'post_details.html', data)


class AddPostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post_page.html"
    success_message="The new blog post has been added"


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        params = {"pk": self.kwargs.get("pk")}
        return reverse_lazy("article-detail", kwargs=params)


class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category_page.html"
    fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "edit_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))


def error_404(request):
    data = {}
    return render(request, 'error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)
