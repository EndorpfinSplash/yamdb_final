from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

v1_router = DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
