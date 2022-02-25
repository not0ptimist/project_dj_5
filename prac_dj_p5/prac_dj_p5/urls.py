from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('market/', include('market.urls')),
]
