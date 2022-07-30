from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

import requests


def init_db(request):
    url = "https://46f95f3a-8415-41f5-8848-c23892b059bb.mock.pstmn.io/movies"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        title_kor = movie["title_kor"]
        title_eng = movie["title_eng"]
        poster_url = movie["poster_url"]
        rating_aud = movie["rating_aud"]
        rating_cri = movie["rating_cri"]
        genre = movie["genre"]
        showtimes = movie["showtimes"]
        release_date = movie["release_date"]
        rate = movie["movie"]
        summary = movie["summary"]
        staff_name = movie["staff"]["name"]
        staff_role = movie["staff"]["role"]
        staff_image_url = movie["staff"]["image_url"]

        movie = {'title_kor': title_kor, 'title_eng':title_eng, 'poster_url':poster_url, 'rating_aud':rating_aud, 'rating_cri':rating_cri, 'genre':genre, 'showtimes':showtimes, 'release_date':release_date, 'rate':rate, 'summary':summary, 'name':staff_name, 'role':staff_role, 'image_url':staff_image_url}
        
        


'''
전체 영화를 조회
'''
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def get_all_movies(request):
    search_movie = request.GET.get('search_movie')
    if search_movie:
        movies = Movie.objects.filter(title_kor__contains=search_movie)
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

