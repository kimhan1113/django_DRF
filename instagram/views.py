from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from instagram.models import Post
from instagram.serializers import PostSerializer



class PublicPostListAPIView(ListCreateAPIView):
    # queryset = Post.objects.filter(is_public=True)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    # 아래 두개의 뷰를 queryset , serializer_class 두개의 정보만의 다 지원함!
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     # print비추, logger 추천
    #
    #     return super().dispatch(request, *args, **kwargs)


# def post_list(request):
#     # 2개 분기
#     pass
#
# def post_detail(request, pk):
#     # request.method -> 3개 분기
#     pass