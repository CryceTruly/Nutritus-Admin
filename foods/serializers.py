from rest_framework import serializers
from .models import Nutrients, FoodsToAvoid


class NutrientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrients
        fields = '__all__'


class FoodsToAvoidSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FoodsToAvoid
