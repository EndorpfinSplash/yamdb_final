from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

v1_router = DefaultRouter()
v1_router.register(r'titles/(?P<title_id>[0-9]+)/reviews',
                   ReviewViewSet,
                   basename='reviews')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
