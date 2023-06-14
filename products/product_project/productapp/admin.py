from django.contrib import admin
from .models import fruits, vegetables, kidsitem
# Register your models here.
admin.site.register(fruits)
admin.site.register(vegetables)
admin.site.register(kidsitem)
