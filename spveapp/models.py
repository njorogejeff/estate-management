from django.db import models


# Create your models here.
class Gender(models.Model):
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.sex


class HseNumber(models.Model):
    house = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.house)


class Position(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class HseOwner(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    id_number = models.PositiveIntegerField()
    mobile_number = models.PositiveIntegerField()
    hse_number = models.ForeignKey(HseNumber, on_delete=models.CASCADE)

    def __str__(self):
        return self.surname


class Occupants(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    hse_number = models.ForeignKey(HseNumber, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname


class Staff(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    id_number = models.PositiveIntegerField()
    mobile_number = models.PositiveIntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname
