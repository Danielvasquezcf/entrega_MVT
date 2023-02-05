
from django.contrib import admin
from django.urls import path
from final_project.views import hello, actual_time, age_view, name, home
from products.views import create_product, list_products, list_categories, create_category


urlpatterns = [
    path('admin/', admin.site.urls),
    #INDEX#
    path('hello/', hello),
    path('today/', actual_time),
    #Cuando queremos que nos mande parametros del front <>#
    path('age/<int:age>/', age_view),
    #Cuando es string ya toma el dato por defecto a diferencia del int#
    path('name/<name>/', name),
    path('home/', home),
    #Crear producto#
    path('create-product/', create_product),
    #listar los productos creados#
    path('list-products/', list_products),
    #Listar las categorias creadas#
    path('list-categories/', list_categories),
    #Crear Categorias#
    path('create-category/<str:name>/', create_category),
]
