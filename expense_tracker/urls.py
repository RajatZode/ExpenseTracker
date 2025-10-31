from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # include all routes from tracker app
    path('', include('tracker.urls')),
]
