from rest_framework import serializers
from .models import Meal, Rating

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description', 'num_of_rating', 'average_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'star', 'user', 'meal')
