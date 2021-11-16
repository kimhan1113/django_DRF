from django.urls import include, path
from rest_framework.routers import DefaultRouter

from instagram.views import PostViewSet, PostDetailAPIView

# from instagram.views import PublicPostListAPIView, public_post_list

router = DefaultRouter()
router.register('post', PostViewSet) # 2개 url을 만들어줌!

urlpatterns = [
    path('mypost/<int:pk>/', PostDetailAPIView.as_view()),
    # path('public/', PublicPostListAPIView.as_view()),
    # path('public/', public_post_list),
    path('', include(router.urls)),
]