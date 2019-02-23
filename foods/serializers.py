from rest_framework import serializers
from .models import Nutrients

class NutrientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nutrients
        fields='__all__'
