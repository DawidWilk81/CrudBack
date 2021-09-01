from rest_framework import serializers
from .models import Film


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ['id', 'Tytul', 'Rezyser', 'Czas_trwania', 'Data_wydania', 'Ocena', 'Oparty_na_ksiazce']
