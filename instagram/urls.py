from django.urls import include, path
from rest_framework.routers import DefaultRouter

from instagram.views import PostViewSet, PublicPostListAPIView

router = DefaultRouter()
router.register('post', PostViewSet) # 2개 url을 만들어줌!

urlpatterns = [
    path('public/', PublicPostListAPIView.as_view()),
    path('', include(router.urls)),
]