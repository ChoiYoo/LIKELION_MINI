from django.shortcuts import redirect, render
from .models import Movie, Comment, Staff
from .serializers import MovieSerializer, CommentSerializer, StaffSerializer
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db.models import Q

import requests

@api_view(['GET'])
def init_db(request):
    url = "https://4026148c-8461-4a65-bbb5-bafce3e2e199.mock.pstmn.io/movie/movielist"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        new_movie = Movie()
        new_movie.title_kor = movie["title_kor"]
        new_movie.title_eng = movie["title_eng"]
        new_movie.poster_url = movie["poster_url"]
        new_movie.rating_aud = movie["rating_aud"]
        new_movie.rating_cri = movie["rating_cri"]
        new_movie.rating_net = movie["rating_net"]
        new_movie.genre = movie["genre"]
        new_movie.showtimes = movie["showtimes"]
        new_movie.release_date = movie["release_date"]
        new_movie.rate = movie["rate"]
        new_movie.summary = movie["summary"]
        new_movie.save()
        for staff in movie["staff"]:
            new_staff = Staff()
            new_staff.movie_title = new_movie
            new_staff.name = staff["name"]
            new_staff.role = staff["role"]
            new_staff.image_url = staff["image_url"]
            new_staff.save()

    return Response(status=status.HTTP_201_CREATED)



'''
전체 영화를 조회
'''
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def get_all_movies(request):
    search_movie = request.GET.get('search_movie')
    if search_movie:
        movies = Movie.objects.filter(Q(title_kor__contains=search_movie) or Q(title_eng__contains=search_movie))
    else:
        movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

'''
영화 세부 조회
'''
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def get_one_movie(request, pk):
    try: 
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def post_one_comment(request):
    serializer = CommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)