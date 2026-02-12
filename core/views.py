from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
import random

def main_page(request):
    menus = Menu.objects.all()
    positions = MenuPosition.objects.all()
    addresses = RestaurantPoint.objects.all()
    contacts = Contacts.objects.all()

    random_position = None
    if positions.exists():
        random_position = random.choice(list(positions))

    context = {
        'menus': menus,
        'positions': positions,
        'addresses': addresses,
        'random_position': random_position,
        'contacts': contacts
    }

    return render(request, 'index.html', context)

def positions_page(request, id):
    menu = Menu.objects.get(id=id)
    positions = menu.positions.all()

    q_search = request.GET.get("search")
    q_sort = request.GET.get("sort")

    if q_search is not None and len(q_search) > 0:
        positions = positions.filter(name__icontains=q_search)

    if q_sort is not None and len(q_sort) > 0:
        if q_sort == "name_asc":
            positions = positions.order_by('name')
        elif q_sort == "name_desc":
            positions = positions.order_by('-name')
        elif q_sort == "price_asc":
            positions = positions.order_by('price')
        elif q_sort == "price_desc":
            positions = positions.order_by('-price')

    positions_count = positions.count()

    per_page = 9
    paginator = Paginator(positions, per_page)
    page_number = request.GET.get("page", 1)

    page_obj = paginator.get_page(page_number)

    context = {
        'menu': menu,
        'positions': page_obj.object_list,
        'page_obj': page_obj,
        'positions_count': positions_count
    }

    return render(request, 'positions.html', context)

