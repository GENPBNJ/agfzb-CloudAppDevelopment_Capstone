from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(max_length=30, primary_key = True)
    description = models.CharField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.name, self.description)



class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, primary_key = True)
    dealerid = models.CharField(max_length=30)
    typeofcar = models.CharField(max_length=30)
    year = models.DateField()

    def __str__(self):
        return "%s %s %s %s" % (self.name, self.dealerid, self.typeofcar, self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
