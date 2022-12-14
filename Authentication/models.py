from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Pengunjung(models.Model):
    class JenisKelamin(models.TextChoices):
        laki_laki = 'LK', 'Male'
        perempuan = 'PP', 'Female'

    user = models.OneToOneField(User, on_delete = models.CASCADE, default = None)
    jenis_kelamin = models.CharField(max_length = 2, choices = JenisKelamin.choices, default = JenisKelamin.laki_laki)
    kontak = models.CharField(max_length = 13, blank = True)
    alamat = models.CharField(max_length = 100, blank = True)
    poin = models.IntegerField(default = 0)



