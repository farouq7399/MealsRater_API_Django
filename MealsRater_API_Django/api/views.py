from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=True, methods=['POST'])
    def meal_rate(self, request, pk=None):
        if 'star' in request.data:
            """
            create or update 
            First get data sent from request and pull from database 
            """
            meal = Meal.objects.get(id=pk)
            star = request.data['star']
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                #create
                rating = Rating.objects.get(user=user.id, meal=meal.id)
                rating.star =star
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Updated',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)
            except:
                #update
                rating = Rating.objects.create(star=star, meal=meal, user=user)
                serializer = RatingSerializer(rating, Many=False)
                json = {
                    'message': " Meal create Created !",
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)

        else:
            json = {
                "message": " Star not provided"
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
