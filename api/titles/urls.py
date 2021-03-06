from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TitleViewSet

v1_router = DefaultRouter()
v1_router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
