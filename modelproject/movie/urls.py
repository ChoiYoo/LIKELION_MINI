from django.urls import path, include
from .views import *


urlpatterns = [
    path('comment/', post_one_comment),
]