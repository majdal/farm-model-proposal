from django.db import models


class Farmer(models.Model):
	capital = models.DecimalField()


class Farm(models.Model):
	geography = models.PolygonField()
	crops = models.ManyToManyField() # e.g. GreenWheat, Corn
	farmer = models.ForeignKey(Farmer)

