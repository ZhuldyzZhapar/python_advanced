from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100, default="red")
    hex_code = models.CharField(max_length=10, default="#FF0000")

    def __str__(self):
        return f"{self.name} color, in hex: {self.hex_code}"


class Car(models.Model):
    name = models.CharField(max_length=100, default="Toyota")
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    width = models.IntegerField(default=200)
    length = models.IntegerField(default=350)

    def __str__(self):
        return f"{self.color.name} {self.name}"
