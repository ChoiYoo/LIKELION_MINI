
from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('', get_all_movies),
	path('<int:pk>/', get_one_movie),
    path('comment/', post_one_comment),
    path('init/', init_db)
]