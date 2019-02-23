from django.urls import reverse
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from .views import index, NutrientsList, NutrientsDetail, create
from .views import FoodCreate, FoodDetail, FoodListView

urlpatterns = [
    path('', FoodListView.as_view(), name='home'),
    path('fcreate', FoodCreate.as_view(), name='fcreate'),
    path('api/nutrients/', NutrientsList.as_view()),
    path("nutrients/<int:pk>/", FoodDetail.as_view(), name="detail"),
    path("api/nutrients/<int:pk>/",
         NutrientsDetail.as_view(), name="nutrient_detail")
]
