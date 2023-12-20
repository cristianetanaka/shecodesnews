from django.urls import path
from .views import (
    IndexView,
    StoryView,
    AddStoryView,
    UpdateStoryView,
    DeleteStoryView,
    like_post,
    AuthorDetailView,
)

app_name = 'news'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', StoryView.as_view(), name='story'),
    path('add-story/', AddStoryView.as_view(), name='newStory'),
    path('author/<str:username>/', AuthorDetailView.as_view(), name='authordetail'),
    path('edit/<int:pk>/', UpdateStoryView.as_view(), name='update_story'),
    path('edit/<int:pk>/remove/', DeleteStoryView.as_view(), name='delete_story'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
]
