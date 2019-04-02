from django.urls import reverse
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from .views import NutrientsList, NutrientsDetail, create
from .views import FoodCreate, FoodDetail, FoodListView, FoodDelete, FoodsToAvoidSiteView, FoodToAvoidDelete, FoodsToAvoidView, FoodToAvoidView


urlpatterns = [
    path('', FoodListView.as_view(), name='home'),
    path('fcreate', FoodCreate.as_view(), name='fcreate'),
    path('ftafoods', FoodsToAvoidSiteView.as_view(), name='ftafoods'),
    path('api/nutrients/', NutrientsList.as_view()),
    path("nutrients/<int:pk>/", FoodDetail.as_view(), name="detail"),
    path("ftafoods/<int:pk>/delete/",
         FoodToAvoidDelete.as_view(), name="del-foodtoavoid"),
    path("nutrients/<int:pk>/delete/", FoodDelete.as_view(), name="del-food"),
    path("api/nutrients/<int:pk>/",
         NutrientsDetail.as_view(), name="nutrient_detail"),

    path("api/foodstoavoid/", FoodsToAvoidView.as_view(), name='foodstoavoid'),
    path("api/foodstoavoid/<int:pk>/",
         FoodToAvoidView.as_view(), name='foodtoavoid'),


]
