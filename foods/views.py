from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Nutrients
from rest_framework.views import APIView
from .serializers import NutrientsSerializer
from rest_framework.response import Response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
# Create your views here.
import json


class FoodListView(LoginRequiredMixin, ListView):
    model = Nutrients
    template_name = 'foods/home.html'
    context_object_name = 'data'
    ordering = ['name']


class FoodDetail(LoginRequiredMixin, DetailView):
    model = Nutrients


class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Nutrients
    success_url = '/'


@login_required()
def create(request):
    return render(request, 'foods/new.html')


class NutrientsList(APIView):
    def get(self, request):
        nutrients = Nutrients.objects.all()
        serializer = NutrientsSerializer(nutrients, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'nutrients': request.data.get('nutrients')
        }
        serializer = NutrientsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class NutrientsDetail(APIView):
    def get(self, request, pk):
        nutrients = get_object_or_404(Nutrients, pk=pk)
        data = NutrientsSerializer(nutrients).data

        return Response(data)


class FoodCreate(CreateView):
    model = Nutrients
    fields = '__all__'
