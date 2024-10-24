from django.urls import path

from apps.views import ImageCreateAPIView, ContactView

urlpatterns = [
    path('image/', ImageCreateAPIView.as_view(), name='image-list'),
    path('contact/', ContactView.as_view(), name='contact')
]
