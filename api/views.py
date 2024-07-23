from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    def delete(self,request, *args, **kwargs):
        Post.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PostListGet(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all()
    serializer_class=PostSerializer
    lookup_field="pk"
# Create your views here.
class GetPostList(APIView):
    def get(self,request,format=None):
        title=request.query_params.get("title","")
        if title:
            post=Post.objects.filter(title__iconatains=True)
        else:
            post=Post.objects.all()
        serializer=PostSerializer(post,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
