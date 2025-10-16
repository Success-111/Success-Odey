from django.urls import path, include
from django.contrib import admin
from . import views  # Import views from the current directory
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bio/', views.bio, name='bio'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('music/', views.music, name='music'),
    path('shop/', views.shop, name='shop'),
    path('tour/', views.tour, name='tour'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#  py -m venv env
#  pip install -r requirements.tx