from django.contrib import admin
from django.urls import path, include
from.views import UserRegisterView

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('blog.urls')),
    #path('members/', include('django.contrib.auth.urls')),
    #path('members/', include('members.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
]
