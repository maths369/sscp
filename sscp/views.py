# Create your views here.
#coding:utf-8

from sscp.models import TFilm
from sscp.serializers import FilmSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class FilmList(APIView):
    def get(self, request, format=None):
        films = TFilm.objects.all()[0:10]
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
