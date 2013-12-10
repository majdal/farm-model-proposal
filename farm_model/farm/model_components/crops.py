from django.db import models


class Crop(models.Model):
	seed = models.CharField()
	equipment = models.CharField()
	carbon = models.DecimalField()
	soil = models.CharField()
	labour = models.DecimalField()

	class Meta:
		abstract = True

class GreenWheat(Crop):
	# specific green wheat related stuff
	pass


class Corn(Crop):
	# specific green wheat related stuff
	pass


