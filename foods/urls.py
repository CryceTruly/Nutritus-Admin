from django.urls import path,include
from .views import index,NutrientsList,NutrientsDetail
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns=[
    path('',index,name='home'),
    path('api/nutrients/',NutrientsList.as_view()),
    path("api/nutrients/<int:pk>/", NutrientsDetail.as_view(), name="nutrient_detail")
]