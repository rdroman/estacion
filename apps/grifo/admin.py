from django.contrib import admin
from apps.grifo.models import Producto, Operador, Cliente
 
admin.site.register(Operador)
admin.site.register(Producto)
admin.site.register(Cliente)