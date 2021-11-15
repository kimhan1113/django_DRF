from django.urls import include, path
from rest_framework.routers import DefaultRouter

from instagram.views import PostViewSet, public_post_list
# from instagram.views import PublicPostListAPIView

router = DefaultRouter()
router.register('post', PostViewSet) # 2개 url을 만들어줌!

urlpatterns = [
    # path('public/', PublicPostListAPIView.as_view()),
    path('public/', public_post_list),
    path('', include(router.urls)),
]