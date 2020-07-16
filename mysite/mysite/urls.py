from django.contrib import admin
from django.urls import path, include
from .views import HomeView, UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('markdownx/', include('markdownx.urls')),
    path('', HomeView.as_view(), name='home'),
]
