from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products, Category

# Aca creamos los productos
def create_product(request):
    #con el Products.objects.(accion que quieras realizar) se crea,se elimina etc etc etc#
    new_product = Products.objects.create(name= 'Rogue Crossfit short', price =15, stock=True)
    print(new_product)
    return HttpResponse('the product was created')

#Para ver la lista de los productos creados#
def list_products(request):
    all_products = Products.objects.all()
    #Para verificar en consola#
    print(all_products)
    #Para mostrar los productos los metemos en el contexto#
    context = {
        'products': all_products
    }
    return render(request, 'list_products.html', context=context)


def create_category(request, name):
    new_category = Category.objects.create(name= name)
    print(new_category)
    return HttpResponse('The category was created!!')
    

def list_categories(request):
    all_categories = Category.objects.all()
    print(all_categories)
    context = {
        'categories': all_categories
    }
    return render(request,'list_categories.html', context=context )