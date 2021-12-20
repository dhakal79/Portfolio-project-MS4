from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('waterchanel.urls')),
    # path('members/', include('django.contrib.auth.urls')),
    # path('members/', include('members.url')),
    path('' , views.home, name="home"),
]
