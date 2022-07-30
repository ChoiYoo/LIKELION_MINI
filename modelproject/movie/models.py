from django.db import models

class Movie(models.Model):
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=900)
    rating_aud = models.CharField(max_length=50)
    rating_cri = models.CharField(max_length=50)
    rating_net = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    showtimes = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    rate = models.CharField(max_length=50)
    summary = models.CharField(max_length=300)

    def __str__(self):
        return self.title_kor

class Staff(models.Model):
    movie_title = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE, related_name='staffs')
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=50)
    image_url = models.CharField(max_length=900)