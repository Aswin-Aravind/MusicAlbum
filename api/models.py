from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator

from django.contrib.auth.models import User



class Album(models.Model):

    title = models.CharField(max_length=200)

    year = models.CharField(max_length=200)

    director = models.CharField(max_length=200)

    language = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)

    @property
    def track_count(self):

        return Track.objects.filter(album=self).count()
    
    @property
    def tracks(self):

        return Track.objects.filter(album=self)
    
    @property
    def review(self):

        return Review.objects.filter(album=self)

    def __str__(self) -> str:

        return self.title




class Track(models.Model):

    title = models.CharField(max_length=200)

    singers = models.CharField(max_length=200)

    genre = models.CharField(max_length=200)

    duration = models.CharField(max_length=100,default=True)

    track_num = models.CharField(max_length=200)

    album = models.ForeignKey(Album,on_delete=models.CASCADE)


    def __str__(self) -> str:

        return self.title


class Review(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    comments = models.CharField(max_length=200)

    rating = models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

