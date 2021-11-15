from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from instagram.models import Post
from instagram.serializers import PostSerializer


# 첫번째 표현

# class PublicPostListAPIView(ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

#     queryset = Post.objects.all()

# 두번째 표현

# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
# public_post_list = PublicPostListAPIView.as_view()

# 세번째 표현

@api_view(['GET'])
def public_post_list(request):

    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)



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