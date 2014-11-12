from rest_framework import generics

from .models import TFilm
from .serializers import *


class FilmList(generics.ListAPIView):
    queryset = TFilm.objects.all()
    serializer_class = FilmSerializer


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TFilm.objects.all()
    serializer_class = FilmSerializer

