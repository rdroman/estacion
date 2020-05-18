from django import forms
from apps.grifo.models import Producto, Operador #, Surtidor

class OperadorForm(forms.ModelForm):
	class Meta:
		model = Operador

		fields = [
			'nombre',
			'apellidos',
			'dni'
		]
		labels = {
			'nombre' : 'Nombre',
			'apellidos' : 'Apellidos',
			'dni' : 'DNI'
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'dni':forms.TextInput(attrs={'class':'form-control'})
		}



class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto

		fields = [
			'descripcion',
			'lado_a',
			'lado_b',
			'stock',
			'precio_venta'
		]
		labels = {
			'descripcion' : 'Descripcion',
			'lado_a' : 'Lado A',
			'lado_b' : 'Lado B',
			'stock' : 'Stock',
			'precio_venta' : 'Precio Venta'
		}
		widgets = {
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'lado_a':forms.NumberInput(attrs={'class':'form-control'}),
			'lado_b':forms.NumberInput(attrs={'class':'form-control'}),
			'stock':forms.NumberInput(attrs={'class':'form-control'}),
			'precio_venta':forms.NumberInput(attrs={'class':'form-control'})
		}



# class SurtidorForm(forms.ModelForm):
# 	class Meta:
# 		model = Surtidor

# 		fields = [
# 			'descripcion',
# 			'producto',
# 			'lado_a',
# 			'lado_b'
# 		]
# 		labels = {
# 			'descripcion' : 'Descripcion',
# 			'producto': 'Producto',
# 			'lado_a' : 'Lado A',
# 			'lado_b' : 'Lado B'
# 		}
# 		widgets = {
# 			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
# 			'producto':forms.Select(attrs={'class':'form-control'}),
# 			'lado_a':forms.NumberInput(attrs={'class':'form-control'}),
# 			'lado_b':forms.NumberInput(attrs={'class':'form-control'})
# 		}


