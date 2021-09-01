from django.db import models

# Create your models here.


class Film(models.Model):
    Ocena = [
        ('A', 'Bardzo dobry'),
        ('B', 'Dobry'),
        ('C', 'Sredni'),
        ('D', 'Slaby'),
        ('E', 'Bardzo slaby'),
        ('F', 'Beznadziejny'),
    ]
    Tytul = models.CharField(default='', max_length=64)
    Rezyser = models.CharField(default='', max_length=64)
    Czas_trwania = models.IntegerField(default=0)
    Data_wydania = models.DateField()
    Ocena = models.CharField(default='Dobry', choices=Ocena, max_length=24)
    Oparty_na_ksiazce = models.BooleanField(default=False)

    def __str__(self):
        return self.Tytul
