
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='homepage'),
    path('admin/', admin.site.urls),
    path('support/', views.support),
    path('users/', include('users.urls')),
    path('', include('campaigns.urls')),

]
if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
