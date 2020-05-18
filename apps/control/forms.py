from django import forms
from apps.control.models import ControlTurno, Despacho, Descuento, \
								Credito, Devolucion, Gasto, Cobranza

class ControlTurnoForm(forms.ModelForm):
	
	class Meta:
		MIS_TURNOS =( 
		    ("1", "Amanecida"), 
		    ("2", "Dia"), 
		    ("3", "Noche"),
	    ) 

		model = ControlTurno

		fields = [
			'fecha',
			'turno',
			'operador',
			'impte_vta_normal',
			'impte_vta_dscto',
			'impte_tot_cobranza',
			'impte_tot_gasto',
			'total_cuenta',
			'total_entrega',
			'diferencia',
			'cerrado'
		]
		labels = {
			'fecha' : 'Fecha',
			'turno' : 'Turno',
			'operador' : 'Operador',
			'impte_vta_normal' : 'Venta Pre.Normal',
			'impte_vta_dscto' : 'Venta Pre.Descuento',
			'impte_tot_cobranza' : 'Total Cobranzas',
			'impte_tot_gasto' : 'Total Gastos',
			'total_cuenta' : 'Cuenta',
			'total_entrega' : 'Entrega',
			'diferencia' : 'Diferencia',
			'cerrado' : 'Cerrado'
		}
		widgets = {
			'fecha': forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'turno':forms.Select(attrs={'class':'form-control'}, choices=MIS_TURNOS),
			'operador' : forms.Select(attrs={'class':'form-control'}),
			'impte_vta_normal':forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'impte_vta_dscto':forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'impte_tot_cobranza':forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'impte_tot_gasto':forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'total_cuenta':forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'total_entrega':forms.NumberInput(attrs={'class':'form-control'}),
			'diferencia':forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'cerrado':forms.HiddenInput()
		}



class DespachoForm(forms.ModelForm):
	
	class Meta:
		model = Despacho

		fields = [
			'turno',
			'producto',
			'lectura_lado_a',
			'lectura_lado_b',
			'gal_despachados',
			'gal_descuento',
			'vta_descuento',
			'gal_credito',
			'vta_credito',
			'gal_devueltos',
			'gal_normal',
			'vta_normal'
		]
		labels = {
			'turno' : 'Turno ID',
			'producto' : 'Producto ID',
			'lectura_lado_a' : 'Lado A',
			'lectura_lado_b' : 'Lado B',
			'gal_despachados': 'Gln.Despachados',
			'gal_descuento' : 'Gln.Descuentos',
			'vta_descuento' : 'Vta.Descuentos',
			'gal_credito' : 'Gln.Creditos',
			'vta_credito' : 'Vta.Creditos',
			'gal_devueltos' : 'Gln.Devueltos',
			'gal_normal' : 'Gln.Pre.Normal',
			'vta_normal' : 'Vta.Pre.Normal'
		}
		widgets = {
			'turno': forms.HiddenInput(),
			'producto' : forms.HiddenInput(),
			'lectura_lado_a': forms.NumberInput(attrs={'class':'form-control'}),
			'lectura_lado_b': forms.NumberInput(attrs={'class':'form-control'}),
			'gal_despachados': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'gal_descuento': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'vta_descuento': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'gal_credito': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'vta_credito': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'gal_devueltos': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'gal_normal': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'vta_normal': forms.NumberInput(attrs={'class':'form-control', 'readonly':True})
		}



class DescuentoForm(forms.ModelForm):
	
	class Meta:
		model = Descuento

		fields = [
			'despacho',
			'producto',
			'precio_dscto',
			'cantidad',
			'monto_dscto',
			'cliente'
		]
		labels = {
			'despacho' : 'Despacho ID',
			'producto' : 'Producto ID',
			'precio_dscto' : 'Pre.Especial',
			'cantidad' : 'Cantidad Glns.',
			'monto_dscto' : 'Monto Descuento',
			'cliente' : 'RUC Cliente'
		}
		widgets = {
			'despacho': forms.HiddenInput(),
			'producto' : forms.HiddenInput(),
			'precio_dscto': forms.NumberInput(attrs={'class':'form-control'}),
			'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
			'monto_dscto': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'cliente': forms.HiddenInput(attrs={'class':'form-control'}),
		}



class CreditoForm(forms.ModelForm):
	
	class Meta:
		model = Credito

		fields = [
			'despacho',
			'cliente',
			'producto',
			'precio_cred',
			'cantidad',
			'monto_cred',
			'monto_cobr',
			'cobrado'
		]
		labels = {
			'despacho' : 'Despacho ID',
			'cliente' : 'Cliente ID',
			'producto' : 'Producto ID',
			'precio_cred' : 'Pre.Credito',
			'cantidad' : 'Cantidad Glns.',
			'monto_cred' : 'Monto Credito',
			'monto_cobr' : 'Monto Cobrado',
			'cobrado' : 'Cobrado'
		}
		widgets = {
			'despacho': forms.HiddenInput(),
			'cliente': forms.HiddenInput(),
			'producto' : forms.HiddenInput(),
			'precio_cred': forms.NumberInput(attrs={'class':'form-control'}),
			'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
			'monto_cred': forms.NumberInput(attrs={'class':'form-control', 'readonly':True}),
			'monto_cobr': forms.HiddenInput(),
			'cobrado': forms.Select(attrs={'class':'form-control', 'default':False})
		}



class DevolucionForm(forms.ModelForm):
	
	class Meta:
		model = Devolucion

		fields = [
			'despacho',
			'producto',
			'cantidad',
		]
		labels = {
			'despacho' : 'Despacho ID',
			'producto' : 'Producto ID',
			'cantidad' : 'Cantidad Glns.',
		}
		widgets = {
			'despacho': forms.TextInput(),
			'producto' : forms.TextInput(),
			'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
		}



class GastoForm(forms.ModelForm):

	class Meta:
		model = Gasto

		fields = [
			'turno',
			'descripcion',
			'monto',
		]
		labels = {
			'turno' : 'Turno ID',
			'descripcion' : 'Descripcion',
			'monto' : 'Monto',
		}
		widgets = {
			'turno': forms.HiddenInput(),
			'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
			'monto': forms.NumberInput(attrs={'class':'form-control'}),
		}



class CobranzaForm(forms.ModelForm):

	class Meta:
		model = Cobranza

		fields = [
			'turno',
			'credito',
			'monto_cobro',
		]
		labels = {
			'turno' : 'Turno ID',
			'credito' : 'Crédito ID',
			'monto_cobro' : 'Monto Cobrado',
		}
		widgets = {
			'turno': forms.HiddenInput(),
			'credito': forms.HiddenInput(),
			'monto_cobro': forms.NumberInput(attrs={'class':'form-control'}),
		}