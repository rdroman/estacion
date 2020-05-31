from django.db import models
from apps.grifo.models import Operador, Producto, Cliente

class ControlTurno(models.Model):
	fecha_registro = models.DateTimeField(auto_now=True)
	fecha = models.DateField()
	turno = models.CharField(max_length=20, blank=True, null=True)
	operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
	impte_vta_normal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
	impte_vta_dscto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
	impte_tot_cobranza = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
	impte_tot_gasto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
	total_cuenta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
	total_entrega = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
	diferencia = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	cerrado = models.BooleanField(default=False)

	def __str__(self):
		return str(self.fecha) + ' ' + (self.operador.nombre)
	
	class Meta:
		ordering = ['-fecha']

	# you override the save method and calculate for total_cuenta
	# def save(self, *args, **kwargs):
	# 	self.total_cuenta = self.impte_vta_normal * self.impte_vta_dscto + self.impte_tot_cobranza - self.impte_tot_gasto;
	# 	self.diferencia = self.total_entrega - self.total_cuenta
	# 	super(ControlTurno, self).save(*args, **kwargs)

class Despacho(models.Model):
	turno = models.ForeignKey(ControlTurno, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now=True)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	lectura_lado_a = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	lectura_lado_b = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	gal_despachados = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	gal_descuento = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	vta_descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
	gal_credito = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	vta_credito = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
	gal_devueltos = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	gal_normal = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	vta_normal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

class Descuento(models.Model):
	despacho = models.ForeignKey(Despacho, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now=True)
	cliente = models.DecimalField(max_digits=11, decimal_places=0, default=0)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	precio_dscto = models.DecimalField(max_digits=8, decimal_places=3, default=0.000)
	cantidad = models.DecimalField(max_digits=8, decimal_places=3, default=0.000)
	monto_dscto = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)

class Credito(models.Model):
	despacho = models.ForeignKey(Despacho, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now=True)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	precio_cred = models.DecimalField(max_digits=8, decimal_places=3, default=0.000)
	cantidad = models.DecimalField(max_digits=8, decimal_places=3, default=0.000)
	monto_cred = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	monto_cobr = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	cobrado = models.BooleanField()

class Devolucion(models.Model):
	despacho = models.ForeignKey(Despacho, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now=True)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.DecimalField(max_digits=8, decimal_places=3, default=0.000)

class Gasto(models.Model):
	turno = models.ForeignKey(ControlTurno, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now=True)
	descripcion = models.CharField(max_length=250, blank=True, null=True)
	monto = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

	class Meta:
		ordering = ['-controlturno__fecha']

class Cobranza(models.Model):
	turno = models.ForeignKey(ControlTurno, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now=True)
	credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
	monto_cobro = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
