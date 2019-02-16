
from django.contrib import admin
from users import views as user_views
from django.urls import path,include
from django.contrib.auth import views as auth_views




admin.site.site_title='Nutritius Admin'
admin.site.site_header = 'Nutritius'

urlpatterns = [
     path('admin/', admin.site.urls),
     path('',include('foods.urls'),name='home'),
     path('profile/', user_views.profile, name='profile'),
     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
      path('',include('accounts.urls')),
     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
]
