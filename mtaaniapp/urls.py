from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='register'),
    path('', include('django.contrib.auth.urls')),
    path('',views.index, name='index'),
    path('logoutuser',views.logoutuser, name='logoutuser'),
    path('profile/',views.profile, name='profile'),
    path('posts/',views.posts, name='posts'),
    path('business/',views.business, name='business'),
    path('business_results/',views.business_results, name='business_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)