from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),  # Ensure 'pk' is a string
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),  # Ensure <int:pk>
    path('delete/<int:pk>', views.delete, name='delete'),  # Ensure <int:pk>
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)