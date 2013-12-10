from django.db import models


class Farm(models.Model):
	geography = models.PolygonField()
	crops = models.ManyToManyField() # e.g. 