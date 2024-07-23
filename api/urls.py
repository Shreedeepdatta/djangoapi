from django.urls import path
from . import views
urlpatterns = [
    path('posts/',views.PostList.as_view(),name='post-view'),
    path('posts/<int:pk>',views.PostListGet.as_view(),name='update-view'),
]
