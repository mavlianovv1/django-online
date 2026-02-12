from django.db import models
from datetime import datetime

# ForeignKey - один-ко-многим - гарем
# ManyToManyField - многие-ко-многим - шведская семья

VOLUME_TYPE_CHOICES = [
    ['ml', 'Миллилитры'],
    ['gr', 'Грамм']
]

class Menu(models.Model):
    image = models.ImageField(upload_to="menus/")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"
    
class MenuTag(models.Model):
    menu = models.ManyToManyField(Menu)
    name = models.CharField(80)

    def __str__(self):
        return f"Тег: {self.name}"
    
class MenuPosition(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="positions")
    image = models.ImageField(upload_to="menus_positions/")
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()
    volume_type = models.CharField(
        choices=VOLUME_TYPE_CHOICES,
        max_length=11
    )

    def __str__(self):
        return f"{self.name} - {self.price} - {self.volume} {self.volume_type}"
    
class MenuIngridient(models.Model):
    menu_position = models.ManyToManyField(MenuPosition, related_name='ingridients')
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"
    

class RestaurantPoint(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building_number = models.CharField(max_length=8)
    phone_number = models.CharField(max_length=30)
    map_url = models.URLField()
    start_time = models.TimeField(default=datetime.now().time())
    end_time = models.TimeField(default=datetime.now().time())

    def __str__(self):
        return f"{self.name} - {self.street}, {self.building_number}"
    
class DayOfWeek(models.Model):
    restaurant_point = models.ManyToManyField(RestaurantPoint, related_name="weekdays")
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Contacts(models.Model):
    phone = models.CharField()
    email = models.EmailField()
    instagram = models.CharField()

    def __str__(self):
        return f"Контакты: {self.phone} {self.email} {self.instagram}"

