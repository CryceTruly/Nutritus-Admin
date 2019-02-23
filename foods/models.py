from django.db import models

class Nutrients(models.Model):
    name=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=500)
    nutrients=models.CharField(max_length=500)


    def get_absolute_url(self):
        return u'/'

    def __str__(self):
        return self.name+" "+self.nutrients

class FoodToAvoid(models.Model):
    name=models.CharField(max_length=255)
    reason=models.CharField(max_length=500)
