
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'movie'

router = DefaultRouter()
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', get_all_movies),
	path('<int:pk>/', get_one_movie),
    path('init/', init_db),
    path('', include(router.urls)),
]