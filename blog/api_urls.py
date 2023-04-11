from django.urls import path

from blog.api_views import PostList, PostDetail
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path
from django.urls import include
from rest_framework.authtoken import views

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)
