from django.contrib import admin
from .models import Menu, MenuPosition, MenuIngridient, MenuTag, RestaurantPoint, DayOfWeek, Contacts

admin.site.register(Menu)
admin.site.register(MenuPosition)
admin.site.register(MenuIngridient)
admin.site.register(MenuTag)
admin.site.register(RestaurantPoint)
admin.site.register(DayOfWeek)
admin.site.register(Contacts)

