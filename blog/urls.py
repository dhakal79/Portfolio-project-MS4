from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView,AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('waterchanel.urls')),
    # path('members/', include('django.contrib.auth.urls')),
    # path('members/', include('members.url')),
    #path('' , views.home, name="home"),
    path('', HomeView.as_view(), name ="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]
