from django.db import models

class Idol(models.Model):
    name = models.CharField(max_length=50)
    yomigana = models.CharField(max_length=50)
    height = models.IntegerField()
    threeSize = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    cv = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name