from rest_framework import viewsets
from .serializers import FilmSerializer
from .models import Film
# Create your views here.


class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
