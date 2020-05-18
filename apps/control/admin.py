from django.contrib import admin
from apps.control.models import ControlTurno, Despacho, Gasto, Descuento, Credito, Cobranza, Devolucion

admin.site.register(ControlTurno)
admin.site.register(Despacho)
admin.site.register(Gasto)
admin.site.register(Descuento)
admin.site.register(Credito)
admin.site.register(Cobranza)
admin.site.register(Devolucion)
