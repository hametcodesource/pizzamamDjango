
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza
# Create your views here.

def index(request):

    """pizzas=Pizza.objects.all()

    pizzas_names_prix=[pizza.nom + ": "+ str(pizza.prix) +" £"for pizza in pizzas]
    #print(pizzas_names)
    pizzas_names_prix_str=",".join(pizzas_names_prix)
    print(pizzas_names_prix_str)
    return HttpResponse('nos pizzas: '+pizzas_names_prix_str)"""

    pizzas=Pizza.objects.all().order_by('prix')
     
    return render(request,'menu/index.html',{'pizzas':pizzas})


def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json=serializers.serialize("json",pizzas)

    return HttpResponse(json)
