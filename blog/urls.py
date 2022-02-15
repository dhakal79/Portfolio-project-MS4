from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView,AddPostView, UpdatePostView, DeletePostView, AddCategoryView, AddCommentView, CategoryView, LikeView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('waterchanel.urls')),
    # path('members/', include('django.contrib.auth.urls')),
    # path('members/', include('members.url')),
    #path('' , views.home, name="home"),
    path('', HomeView.as_view(), name ="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>' LikeView, name='like_post'),    
]
