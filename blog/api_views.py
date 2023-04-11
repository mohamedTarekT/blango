import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from blog.api.serializers import PostSerializer
from rest_framework.response import Response
from blog.models import Post
from rest_framework import generics

from rest_framework.decorators import api_view


# def post_to_dict(post):
#     return {
#         "pk": post.pk,
#         "author_id": post.author_id,
#         "created_at": post.created_at,
#         "modified_at": post.modified_at,
#         "published_at": post.published_at,
#         "title": post.title,
#         "slug": post.slug,
#         "summary": post.summary,
#         "content": post.content,
#     }


# @csrf_exempt
# @api_view(["GET", "POST"])
# def post_list(request, format = None):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         return JsonResponse({"data": PostSerializer(posts, many=True).data})
#     elif request.method == "POST":
#         post_data = json.loads(request.body)
#         serializer = PostSerializer(data=post_data)
#         serializer.is_valid(raise_exception=True)
#         post = serializer.save()
#         return HttpResponse(
#             status=HTTPStatus.CREATED,
#             headers={"Location": reverse("api_post_detail", args=(post.pk,))},
#         )
#
#     return HttpResponseNotAllowed(["GET", "POST"])

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer





# @csrf_exempt
# @api_view(["GET", "PUT", "DELETE"])
# def post_detail(request, pk, format =None):
#     # post = get_object_or_404(Post, pk=pk)
#     try:
#       post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#       return Response(status=HTTPStatus.NOT_FOUND)
#     if request.method == "GET":
#         return Response(PostSerializer(post).data)
#     elif request.method == "PUT":
#         # post_data = json.loads(request.body)
#         # serializer = PostSerializer(post, data=post_data)
#         serializer = PostSerializer(post, data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=HTTPStatus.NO_CONTENT)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response(status=HTTPStatus.NO_CONTENT)
#
#     return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])

# class PostDetail(APIView):
#     @staticmethod
#     def get_post(pk):
#         return get_object_or_404(Post, pk=pk)
#
#     def get(self, request, pk, format=None):
#         post = self.get_post(pk)
#         return Response(PostSerializer(post).data)
#
#     def put(self, request, pk, format=None):
#         post = self.get_post(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=HTTPStatus.NO_CONTENT)
#         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         post = self.get_post(pk)
#         post.delete()
#         return Response(status=HTTPStatus.NO_CONTENT)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer