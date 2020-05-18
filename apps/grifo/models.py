from django.db import models

class Cliente(models.Model):
	fecha_registro = models.DateTimeField(auto_now=True)
	razonsocial = models.CharField(max_length=250, blank=True, null=True)
	ruc = models.DecimalField(max_digits=11, decimal_places=0, default=0)

	def __str__(self):
		return self.razonsocial

	class Meta:
		ordering = ['razonsocial']

class Producto(models.Model):
	fecha_registro = models.DateTimeField(auto_now=True)
	descripcion = models.CharField(max_length=50, blank=True, null=True)
	lado_a = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	lado_b = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	stock = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
	precio_venta = models.DecimalField(max_digits=8, decimal_places=3, default=0.000)

	def __str__(self):
		return self.descripcion

# class Surtidor(models.Model):
# 	descripcion = models.CharField(max_length=50, blank=True, null=True)
# 	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	
# 	def __str__(self):
# 		return self.descripcion + ' ' + self.producto.descripcion

# 	#def _get_total_gal_normal(self):
# 	#	return self.tot_gal_atendidos - self.tot_gal_descuento - self.tot_gal_creditos - self.tot_gal_devueltos
# 	#
# 	#tot_gal_normal = property(_get_total_gal_normal)



class Operador(models.Model):
	fecha_registro = models.DateTimeField(auto_now=True)
	nombre = models.CharField(max_length=50, blank=True, null=True)
	apellidos = models.CharField(max_length=100, blank=True, null=True)
	dni = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return self.nombre + ' ' + self.apellidos
