from django.db import models

class Nutrients(models.Model):
    name=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=500)
    nutrients=models.CharField(max_length=500)

    def __str__(self):
        return self.name+" "+self.nutrients
