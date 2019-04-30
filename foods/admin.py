from django.contrib import admin

from django.contrib.admin import AdminSite
from .models import RecommendedFood, FoodsToAvoid


class MyModelAdmin(admin.ModelAdmin):
    view_on_site = False

# Register your models here.
admin.site.register(RecommendedFood, MyModelAdmin)
admin.site.register(FoodsToAvoid, MyModelAdmin)


class MyAdminSite(AdminSite):
    # Disable View on Site link on admin page
    site_url = None
