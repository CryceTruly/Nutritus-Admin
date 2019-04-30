from rest_framework import serializers
from .models import RecommendedFood, FoodsToAvoid


class NutrientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedFood
        fields = '__all__'


class FoodsToAvoidSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FoodsToAvoid
