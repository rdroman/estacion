from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.control.forms import ControlTurnoForm, DespachoForm, DescuentoForm, CreditoForm, DevolucionForm, GastoForm, CobranzaForm
from apps.control.models import ControlTurno, Despacho, Descuento, Credito, Devolucion, Gasto, Cobranza
from apps.grifo.models import Producto, Cliente
from django.core import serializers
from decimal import Decimal

# Create your views here.
def index(request):
	return render(request, 'control/index.html')



class TurnoList(ListView):
	model = ControlTurno
	template_name = 'control/ctllst.html'




class TurnoDetalle(ListView):
	model = ControlTurno
	template_name = 'control/ctldet.html'

	def get_context_data(self, **kwargs):
		context = super(TurnoDetalle, self).get_context_data(**kwargs)
		pkturno = self.kwargs.get('pk', 0)
		miobjTurno = self.model.objects.get(id = pkturno)
		misDespTurno = Despacho.objects.all().filter(turno = pkturno)

		context['miobjTurno'] = miobjTurno
		context['misDespTurno'] = misDespTurno
		context['pkturno'] = pkturno
		return context


# class ControlTurnoCreate(CreateView):
# 	model = ControlTurno
# 	template_name = 'control/ctladd.html'
# 	form_class = ControlTurnoForm
# 	second_form_class = OperadorForm
# 	success_url = reverse_lazy('control:ctllst')

# 	def get_context_data(self, **kwargs):
# 		context = super(ControlTurnoCreate, self).get_context_data(**kwargs)
# 		if 'form' not in context:
# 			context['form'] = self.form_class(self.request.GET)
# 		if 'form2' not in context:
# 			context['form2'] = self.second_form_class(self.request.GET)
# 		return context

# 	def post(self, request, *args, **kwargs):
# 		self.object = self.get_object
# 		form = self.form_class(request.POST)
# 		form2 = self.second_form_class(request.POST)

# 		if form.is_valid() and form2.is_valid():
# 			tmpvar_control = form.save(commit=False)
# 			tmpvar_control.operador = form2.save()
# 			tmpvar_control.save()
# 			return HttpResponseRedirect(self.get_success_url())
# 		else:
# 			return self.render_to_response(self.get_context_data(form=form, form2=form2))




# class ControlTurnoUpdate(UpdateView):
# 	model = ControlTurno
# 	second_model = Operador
# 	template_name = 'control/ctladd.html'
# 	form_class = ControlTurnoForm
# 	second_form_class = OperadorForm
# 	success_url = reverse_lazy('control:ctllst')

# 	def get_context_data(self, **kwargs):
# 		context = super(ControlTurnoUpdate, self).get_context_data(**kwargs)
# 		pk = self.kwargs.get('pk', 0)
# 		tmpvar_miturno = self.model.objects.get(id=pk)
# 		tmpvar_operador = self.second_model.objects.get(id=tmpvar_miturno.operador_id)
# 		if 'form' not in context:
# 			context['form'] = self.form_class(self.request.GET)
# 		if 'form2' not in context:
# 			context['form2'] = self.second_form_class(instance=tmpvar_operador)
# 		context['id'] = pk
# 		return context

# 	def post(self, request, *args, **kwargs):
# 		self.object = self.get_object
# 		id_control = kwargs['pk']
# 		tmpvar_micontrol = self.model.objects.get(id = id_control)
# 		tmpvar_mioperador = self.second_model.objects.get(id = tmpvar_micontrol.operador_id)
# 		form = self.form_class(request.POST, instance = tmpvar_micontrol)
# 		form2 = self.second_form_class(request.POST, instance = tmpvar_mioperador)
# 		if form.is_valid() and form2.is_valid():
# 			form.save()
# 			form2.save()
# 			return HttpResponseRedirect(self.get_success_url())
# 		else:
# 			return HttpResponseRedirect(self.get_success_url())



# def TurnoCrear(request):
# 	if request.method == 'POST':
# 		form = ControlTurnoForm(request.POST)
# 		if form.is_valid():
# 			new_control = form.save()
# 			return HttpResponseRedirect(reverse_lazy('control:dsplst', kwargs={'mipk':new_control.id}))
# 	else:
# 		form = ControlTurnoForm()
# 		return render(request, 'control/ctladd.html', {'form': form})



class TurnoCreate(CreateView):
	model = ControlTurno
	form_class = ControlTurnoForm
	template_name = 'control/ctladd.html'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			tmpvar_turno = form.save() #Guarda el formulario y asigna el PK a la variable temporal

			#Hacemos un print de los valores que se han guardado
			for campo in form:
				print(campo.name,'=', str(campo.value()))

			#Vamos al Despacho Listar
			return HttpResponseRedirect(reverse_lazy('control:dsplst', kwargs={'mipk':tmpvar_turno.id}))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))




class TurnoUpdate(UpdateView):
	model = ControlTurno
	form_class = ControlTurnoForm
	template_name = 'control/ctladd.html'

	def get_context_data(self, **kwargs):
		context = super(TurnoUpdate, self).get_context_data(**kwargs)
		pkturno = self.kwargs.get('pk',0) #Este es el PK del modelo ControlTurno enviado por URL.py
		tmpvar_turno = self.model.objects.get(id=pkturno) #Consultamos el modelo ControlTurno con el ID obtenido 

		#Creamos el form que va a existir en el html
		if 'form' not in context:
			context['form'] = self.form_class(instance = tmpvar_turno)

		context['pkturno'] = pkturno
		#context['tmpvar_turno'] = tmpvar_turno
		return context

	def post(self, request, *args, **kwargs):
		request.POST._mutable = True #Para cambiar valores del POST en el form 
		self.object = self.get_object
		pkturno = kwargs['pk']
		print ('mi pk turno ----------> ', pkturno)
		tmpvar_turno = self.model.objects.get(id = pkturno)
		form = self.form_class(request.POST, instance = tmpvar_turno)
		form.data['cerrado'] = True

		if form.is_valid():
			objTurno = form.save()
			
			#Actualizamos las lecturas de los Despachos
			objMisDespachos = Despacho.objects.all().filter(turno = pkturno)
			for midesp in objMisDespachos:
				nva_lect_a = midesp.lectura_lado_a
				nva_lect_b = midesp.lectura_lado_b
				nvo_stock = midesp.producto.stock - midesp.gal_despachados
				Producto.objects.filter(id = midesp.producto.id).update(lado_a = nva_lect_a,
																		lado_b = nva_lect_b,
																		stock = nvo_stock )
			#Regresamos al Despacho Listar
			return HttpResponseRedirect(reverse_lazy('control:ctllst'))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))




class DespachoList(ListView):
	model = Despacho
	form_class = DespachoForm
	template_name = 'control/dsplst.html'
	success_url = reverse_lazy('control:dspadd')

	def get_context_data(self, **kwargs):
		context = super(DespachoList, self).get_context_data(**kwargs)
		pk = self.kwargs.get('mipk', 0)
		midespacho_turno = self.model.objects.all().filter(turno=pk)
		misproductos = Producto.objects.all()
		context['midespacho_turno'] = midespacho_turno
		context['mis_prods'] = misproductos
		context['controlpk'] = pk
		return context

	def post(self, request, *args, **kwargs):
		micontrol = request.POST.get('controlpk')
		miproducto = request.POST.get('selprodnm')
		return HttpResponseRedirect(reverse_lazy('control:dspadd', kwargs={'micontrol':micontrol, 'miproducto':miproducto}))



class DespachoCreate(CreateView):
	model = Despacho
	form_class = DespachoForm
	template_name = 'control/dspadd.html'

	# def get_queryset(self):
	# 	mi_consulta = Producto.objects.all()
	# 	lista_productos = []
	# 	for itm in mi_consulta:
	# 		lista_productos.append({'prod':itm.descripcion, 'lect_a': itm.lado_a, 'lect_b': itm.lado_b})

	def get_context_data(self, **kwargs):
		context = super(DespachoCreate, self).get_context_data(**kwargs)
		pk_control = self.kwargs.get('micontrol', 0) #Trae los kwargs enviados como diccionario en el reverselazy que llama a este formulario
		pk_producto = self.kwargs.get('miproducto', 0) #Trae los kwargs enviados como diccionario en el reverselazy que llama a este formulario
		miproducto = Producto.objects.get(id=pk_producto) #Hago una consulta al modelo Producto

		#Creamos el form que va a existir en el html
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		
		context['idcontrol'] = pk_control
		context['idproducto'] = pk_producto
		context['miproducto'] = miproducto
		context['iddespacho'] = 0
		return context

	def post(self, request, *args, **kwargs):
		request.POST._mutable = True #Para cambiar valores del POST en el form 
		self.object = self.get_object
		form = self.form_class(request.POST)
		micontrol = request.POST.get('txtpkcontrol') #Valores enviados por la URL
		miproducto = request.POST.get('txtProdID') #Valores enviados por la URL
		print("--------------- recoge parametros.... micontrol: ", micontrol)
		print("--------------- recoge parametros.... miproducto: ", miproducto)
		form.data['turno'] = micontrol #Cambia el valor del campo 'turno' del form 
		form.data['producto'] = miproducto #Cambia el valor del campo 'producto' del form 
		
		print("------------------- pase")
		if form.is_valid():
			tmpvar_despacho = form.save() #Guarda el formulario y asigna el PK a la variable temporal

			#Hacemos un print de los valores que se han guardado
			for campo in form:
				print(campo.name,'=', str(campo.value()))

			#### ESTO OK >> (AL PROCESAR MEJOR) ###Producto.objects.filter(id=miproducto).update(lado_a=str(form['lectura_lado_a'].value()), lado_b=str(form['lectura_lado_b'].value()))

			#Regresamos al Despacho Listar
			return HttpResponseRedirect(reverse_lazy('control:dsplst', kwargs={'mipk':micontrol}))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))



class DespachoUpdate(UpdateView):
	model = Despacho
	form_class = DespachoForm
	template_name = 'control/dspadd.html'

	def get_context_data(self, **kwargs):
		context = super(DespachoUpdate, self).get_context_data(**kwargs)
		pkdespa = self.kwargs.get('pk',0) #Este es el PK del modelo Despacho enviado por URL.py
		tmpvar_despacho = self.model.objects.get(id=pkdespa) #Consultamos el modelo Despacho con el ID obtenido 
		miproducto = Producto.objects.get(id=tmpvar_despacho.producto_id) #Filtramos por ID Producto del Modelo Despacho

		#Creamos el form que va a existir en el html
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)

		context['idcontrol'] = tmpvar_despacho.turno_id
		context['idproducto'] = tmpvar_despacho.producto_id
		context['miproducto'] = miproducto
		context['iddespacho'] = pkdespa
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		pkdespa = kwargs['pk'] #Este es el PK del formulario (modelo Despacho)
		tmpvar_despacho = self.model.objects.get(id = pkdespa)
		form = self.form_class(request.POST, instance = tmpvar_despacho)
		
		if form.is_valid():
			miobjdespacho = form.save() #Guarda el formulario y asigna el PK a la variable miobjdespacho

			#Hacemos un print de los valores que se han guardado
			for campo in form:
				print(campo.name,'=', str(campo.value()))

			#Actualizamos los montos del Turno
			objTurno = ControlTurno.objects.get(id = tmpvar_despacho.turno_id)
			vta_norm = objTurno.impte_vta_normal
			vta_dcto = objTurno.impte_vta_dscto
			vta_dcto = vta_dcto + miobjdespacho.vta_descuento
			vta_norm = vta_norm + miobjdespacho.vta_normal
			ControlTurno.objects.filter(id=tmpvar_despacho.turno_id).update(
															impte_vta_dscto = vta_dcto,
															impte_vta_normal = vta_norm )

			#Regresamos al Despacho Listar
			return HttpResponseRedirect(reverse_lazy('control:dsplst', kwargs={'mipk':tmpvar_despacho.turno_id}))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))




class DespachoDelete(DeleteView):
	model = Despacho
	template_name = 'control/dspdel.html'
	#success_url = reverse_lazy('control:ctllst') #Esto ya no es necesario cuando redefinimos el metodo (abajo)

	def get_success_url(self):
		pkcontrol = self.request.POST.get('txtTurnoID')  #Obtenemos el pk del turno, para poder volver al listado
		impte_vtadcto = Decimal(self.request.POST.get('txtfrmdsp_vtadcto'))
		impte_vtanorm = Decimal(self.request.POST.get('txtfrmdsp_vtanorm'))

		#Actualizamos los montos del Turno
		objTurno = ControlTurno.objects.get(id = pkcontrol)
		vta_norm = objTurno.impte_vta_normal
		vta_dcto = objTurno.impte_vta_dscto
		vta_dcto = vta_dcto - impte_vtadcto
		vta_norm = vta_norm - impte_vtanorm
		ControlTurno.objects.filter(id=tmpvar_despacho.turno_id).update(impte_vta_dscto = vta_dcto,
																		impte_vta_normal = vta_norm )

		return reverse('control:dsplst', kwargs={'mipk': pkcontrol} )




class DescuentoList(ListView):
	model = Descuento
	form_class = DescuentoForm
	template_name = 'control/dctlst.html'
	success_url = reverse_lazy('control:dctadd')

	def get_context_data(self, **kwargs):
		context = super(DescuentoList, self).get_context_data(**kwargs)
		pkdesp = self.kwargs.get('midespacho', 0)
		pkprod = self.kwargs.get('miproducto', 0)
		midescuentos_despacho = self.model.objects.all().filter(despacho=pkdesp, producto=pkprod)
		miproducto = Producto.objects.get(id=pkprod)
		
		context['midescuentos_despacho'] = midescuentos_despacho
		context['mi_prod'] = miproducto
		context['iddespacho'] = pkdesp
		return context

	def post(self, request, *args, **kwargs):
		midespacho = request.POST.get('txtiddespacho')
		miproducto = request.POST.get('lblidproducto')
		return HttpResponseRedirect(reverse_lazy('control:dctadd', kwargs={'pkdespacho':midespacho, 'pkproducto':miproducto}))




class DescuentoCreate(CreateView):
	model = Descuento
	form_class = DescuentoForm
	template_name = 'control/dctadd.html'
	success_url = reverse_lazy('control:dctlst')

	def get_context_data(self, **kwargs):
		context = super(DescuentoCreate, self).get_context_data(**kwargs)
		pkdesp = self.kwargs.get('pkdespacho', 0)
		pkprod = self.kwargs.get('pkproducto', 0)
		misclientes = Cliente.objects.all()

		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)

		context['iddespacho'] = pkdesp
		context['idproducto'] = pkprod
		context['misclientes'] = misclientes
		return context

	def post(self, request, *args, **kwargs):
		request.POST._mutable = True #Para cambiar valores del POST en el form 
		self.object = self.get_object
		form = self.form_class(request.POST)
		midespacho = request.POST.get('hdndcto_pkdespacho') #Valores enviados en el submit
		miproducto = request.POST.get('hdndcto_pkproducto') #Valores enviados en el submit
		form.data['despacho'] = midespacho #Cambia el valor del campo 'despacho' del form 
		form.data['producto'] = miproducto #Cambia el valor del campo 'producto' del form 
		
		if form.is_valid():
			tmpvar_descuento = form.save() #Guarda el formulario y asigna el PK a la variable temporal

			#Hacemos un print de los valores que se han guardado
			for campo in form:
				print(campo.name,'=', str(campo.value()))

			objDespacho = Despacho.objects.get(id=midespacho)
			cant_dscto_desp = objDespacho.gal_descuento
			mont_dscto_desp = objDespacho.vta_descuento
			cant_dscto_desp = cant_dscto_desp + tmpvar_descuento.cantidad
			mont_dscto_desp = mont_dscto_desp + tmpvar_descuento.monto_dscto

			#Actualizamos la cantidad de galones y venta, realizadas con descuento 
			Despacho.objects.filter(id=midespacho).update(gal_descuento = cant_dscto_desp, 
														  vta_descuento = mont_dscto_desp)
			
			#Regresamos al Despacho Listar
			return HttpResponseRedirect(reverse_lazy('control:dctlst', kwargs={'midespacho':midespacho, 'miproducto':miproducto}))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))




class DescuentoDelete(DeleteView):
	model = Descuento
	template_name = 'control/dctdel.html'
	#success_url = reverse_lazy('control:ctllst') #Esto ya no es necesario cuando redefinimos el metodo (abajo)

	def get_success_url(self):
		pkdespacho = self.request.POST.get('txtfrmdscto_despachoid')  #Obtenemos el pk del despacho
		pkproducto = self.request.POST.get('txtfrmdscto_productoid')  #Obtenemos el pk del producto
		cant_dcto = Decimal(self.request.POST.get('txtfrmdscto_cantdcto'))
		monto_dcto = Decimal(self.request.POST.get('txtfrmdscto_monto'))
		
		#Restamos los galones y monto de descuento en el Form Despacho
		objDespacho = Despacho.objects.get(id=pkdespacho)
		cant_dscto_desp = objDespacho.gal_descuento
		mont_dscto_desp = objDespacho.vta_descuento
		cant_dscto_desp = cant_dscto_desp - cant_dcto
		mont_dscto_desp = mont_dscto_desp - monto_dcto

		#Actualizamos la cantidad de galones y venta: 
		Despacho.objects.filter(id=pkdespacho).update(gal_descuento = cant_dscto_desp, 
													  vta_descuento = mont_dscto_desp)
		return reverse('control:dctlst', kwargs={'midespacho': pkdespacho, 'miproducto':pkproducto})

	def get_context_data(self, **kwargs):
		context = super(DescuentoDelete, self).get_context_data(**kwargs)
		pkdcto = self.kwargs.get('pk', 0)
		objdescuento = self.model.objects.get(id = pkdcto)
		objcliente = Cliente.objects.get(ruc = objdescuento.cliente)

		context['objdescuento'] = objdescuento
		context['objcliente'] = objcliente
		return context




class CreditoList(ListView):
	model = Credito
	form_class = CreditoForm
	template_name = 'control/crelst.html'
	success_url = reverse_lazy('control:creadd')

	def get_context_data(self, **kwargs):
		context = super(CreditoList, self).get_context_data(**kwargs)
		pkdesp = self.kwargs.get('midespacho', 0)
		pkprod = self.kwargs.get('miproducto', 0)
		micreditos_despacho = self.model.objects.all().filter(despacho=pkdesp, producto=pkprod)
		miproducto = Producto.objects.get(id=pkprod)
		
		context['micreditos_despacho'] = micreditos_despacho
		context['mi_prod'] = miproducto
		context['iddespacho'] = pkdesp
		return context

	def post(self, request, *args, **kwargs):
		midespacho = request.POST.get('txtiddespacho')
		miproducto = request.POST.get('lblidproducto')
		return HttpResponseRedirect(reverse_lazy('control:creadd', kwargs={'pkdespacho':midespacho, 'pkproducto':miproducto}))




class CreditoCreate(CreateView):
	model = Credito
	form_class = CreditoForm
	template_name = 'control/creadd.html'
	success_url = reverse_lazy('control:crelst')

	def get_context_data(self, **kwargs):
		context = super(CreditoCreate, self).get_context_data(**kwargs)
		pkdesp = self.kwargs.get('pkdespacho', 0)
		pkprod = self.kwargs.get('pkproducto', 0)
		misclientes = Cliente.objects.all()

		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)

		context['iddespacho'] = pkdesp
		context['idproducto'] = pkprod
		context['misclientes'] = misclientes
		return context

	def post(self, request, *args, **kwargs):
		request.POST._mutable = True #Para cambiar valores del POST en el form 
		self.object = self.get_object
		form = self.form_class(request.POST)
		midespacho = request.POST.get('hdncred_pkdespacho') #Valores enviados en el submit
		miproducto = request.POST.get('hdncred_pkproducto') #Valores enviados en el submit
		form.data['despacho'] = midespacho #Cambia el valor del campo 'despacho' del form 
		form.data['producto'] = miproducto #Cambia el valor del campo 'producto' del form 
		
		if form.is_valid():
			tmpvar_credito = form.save() #Guarda el formulario y asigna el PK a la variable temporal

			#Hacemos un print de los valores que se han guardado
			for campo in form:
				print(campo.name,'=', str(campo.value()))

			objDespacho = Despacho.objects.get(id=midespacho)
			cant_cred_desp = objDespacho.gal_credito
			mont_cred_desp = objDespacho.vta_credito
			cant_cred_desp = cant_cred_desp + tmpvar_credito.cantidad
			mont_cred_desp = mont_cred_desp + tmpvar_credito.monto_cred

			#Actualizamos la cantidad de galones y venta, realizadas con descuento 
			Despacho.objects.filter(id=midespacho).update(gal_credito = cant_cred_desp, 
														  vta_credito = mont_cred_desp)
			
			#Regresamos al Despacho Listar
			return HttpResponseRedirect(reverse_lazy('control:crelst', kwargs={'midespacho':midespacho, 'miproducto':miproducto}))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))




class CreditoDelete(DeleteView):
	model = Credito
	template_name = 'control/credel.html'
	
	def get_success_url(self):
		pkdespacho = self.request.POST.get('txtfrmcred_despachoid')  #Obtenemos el pk del despacho
		pkproducto = self.request.POST.get('txtfrmcred_productoid')  #Obtenemos el pk del producto
		cant_cred = Decimal(self.request.POST.get('txtfrmcred_cantcred'))
		monto_cred = Decimal(self.request.POST.get('txtfrmcred_monto'))
		
		#Restamos los galones y monto de descuento en el Form Despacho
		objDespacho = Despacho.objects.get(id=pkdespacho)
		cant_cred_desp = objDespacho.gal_credito
		mont_cred_desp = objDespacho.vta_credito
		cant_cred_desp = cant_cred_desp - cant_cred
		mont_cred_desp = mont_cred_desp - monto_cred

		#Actualizamos la cantidad de galones y venta: 
		Despacho.objects.filter(id=pkdespacho).update(gal_credito = cant_cred_desp, 
													  vta_credito = mont_cred_desp)
		return reverse('control:crelst', kwargs={'midespacho': pkdespacho, 'miproducto':pkproducto})

	def get_context_data(self, **kwargs):
		context = super(CreditoDelete, self).get_context_data(**kwargs)
		pkcred = self.kwargs.get('pk', 0)
		objcredito = self.model.objects.get(id = pkcred)
		context['objcredito'] = objcredito
		return context



class DevolucionList(ListView):
	model = Devolucion
	form_class = DevolucionForm
	template_name = 'control/devlst.html'
	success_url = reverse_lazy('control:devadd')

	def get_context_data(self, **kwargs):
		context = super(DevolucionList, self).get_context_data(**kwargs)
		pkdesp = self.kwargs.get('midespacho', 0)
		pkprod = self.kwargs.get('miproducto', 0)
		midevolucion_despacho = self.model.objects.all().filter(despacho=pkdesp, producto=pkprod)
		miproducto = Producto.objects.get(id=pkprod)
		
		context['midevolucion_despacho'] = midevolucion_despacho
		context['mi_prod'] = miproducto
		context['iddespacho'] = pkdesp
		return context

	def post(self, request, *args, **kwargs):
		midespacho = request.POST.get('txtiddespacho')
		miproducto = request.POST.get('lblidproducto')
		return HttpResponseRedirect(reverse_lazy('control:devadd', kwargs={'pkdespacho':midespacho, 'pkproducto':miproducto}))




class DevolucionCreate(CreateView):
	model = Devolucion
	form_class = DevolucionForm
	template_name = 'control/devadd.html'
	success_url = reverse_lazy('control:devlst')

	def get_context_data(self, **kwargs):
		context = super(DevolucionCreate, self).get_context_data(**kwargs)
		pkdesp = self.kwargs.get('pkdespacho', 0)
		pkprod = self.kwargs.get('pkproducto', 0)
		
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)

		context['iddespacho'] = pkdesp
		context['idproducto'] = pkprod
		return context

	def post(self, request, *args, **kwargs):
		request.POST._mutable = True #Para cambiar valores del POST en el form 
		self.object = self.get_object
		form = self.form_class(request.POST)
		midespacho = request.POST.get('hdndev_pkdespacho') #Valores enviados en el submit
		miproducto = request.POST.get('hdndev_pkproducto') #Valores enviados en el submit
		form.data['despacho'] = midespacho #Cambia el valor del campo 'despacho' del form 
		form.data['producto'] = miproducto #Cambia el valor del campo 'producto' del form 
		
		if form.is_valid():
			tmpvar_devolucion = form.save() #Guarda el formulario y asigna el PK a la variable temporal

			#Hacemos un print de los valores que se han guardado
			for campo in form:
				print(campo.name,'=', str(campo.value()))

			objDespacho = Despacho.objects.get(id=midespacho)
			cant_dev_desp = objDespacho.gal_devueltos
			cant_dev_desp = cant_dev_desp + tmpvar_devolucion.cantidad
			
			#Actualizamos la cantidad de galones devueltos al tanque 
			Despacho.objects.filter(id=midespacho).update(gal_devueltos = cant_dev_desp)
			
			#Regresamos al Devolucion Listar
			return HttpResponseRedirect(reverse_lazy('control:devlst', kwargs={'midespacho':midespacho, 'miproducto':miproducto}))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))




class DevolucionDelete(DeleteView):
	model = Devolucion
	template_name = 'control/devdel.html'
	
	def get_success_url(self):
		pkdespacho = self.request.POST.get('txtfrmdev_despachoid')  #Obtenemos el pk del despacho
		pkproducto = self.request.POST.get('txtfrmdev_productoid')  #Obtenemos el pk del producto
		cant_dev = Decimal(self.request.POST.get('txtfrmdev_cantdev'))
		
		#Restamos los galones y monto de descuento en el Form Despacho
		objDespacho = Despacho.objects.get(id=pkdespacho)
		cant_dev_desp = objDespacho.gal_devueltos
		cant_dev_desp = cant_dev_desp - cant_dev
		
		#Actualizamos la cantidad de galones y venta: 
		Despacho.objects.filter(id=pkdespacho).update(gal_devueltos = cant_dev_desp)
		return reverse('control:devlst', kwargs={'midespacho': pkdespacho, 'miproducto':pkproducto})

	def get_context_data(self, **kwargs):
		context = super(DevolucionDelete, self).get_context_data(**kwargs)
		pkdev = self.kwargs.get('pk', 0)
		objdevolucion = self.model.objects.get(id = pkdev)
		context['objdevolucion'] = objdevolucion
		return context




class GastoList(ListView):
	model = Gasto
	form_class = GastoForm
	template_name = 'control/gtolst.html'

	def get_context_data(self, **kwargs):
		context = super(GastoList, self).get_context_data(**kwargs)
		pkturno = self.kwargs.get('micontrol', 0)
		misgastos_turno = self.model.objects.all().filter(turno=pkturno)
		context['pkturno'] = pkturno
		context['misgastos_turno'] = misgastos_turno
		return context





class GastoCreate(CreateView):
	model = Gasto
	form_class = GastoForm
	template_name = 'control/gtoadd.html'

	def get_context_data(self, **kwargs):
		context = super(GastoCreate, self).get_context_data(**kwargs)
		pkturno = self.kwargs.get('micontrol', 0)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		context['pkturno'] = pkturno
		return context

	def post(self, request, *args, **kwargs):
		request.POST._mutable = True #Para cambiar valores del POST en el form 
		self.object = self.get_object
		form = self.form_class(request.POST)
		pkturno = self.request.POST.get('txtidturno_gto')  #Obtenemos el pk del Turno
		form.data['turno'] = pkturno #Cambia el valor del campo 'Turno' del form 

		if form.is_valid():
			tmpvar_gasto = form.save() #Guarda el formulario y asigna el PK a la variable temporal

			#Hacemos un print de los valores que se han guardado
			for campo in form:
				print(campo.name,'=', str(campo.value()))

			#Actualizamos los montos del Turno
			objTurno = ControlTurno.objects.get(id = pkturno)
			tot_gasto = objTurno.impte_tot_gasto
			tot_gasto = tot_gasto + tmpvar_gasto.monto
			ControlTurno.objects.filter(id=pkturno).update(impte_tot_gasto = tot_gasto)


			#Regresamos al Devolucion Listar
			return HttpResponseRedirect(reverse_lazy('control:gtolst', kwargs={'micontrol':pkturno}))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))




class GastoDelete(DeleteView):
	model = Gasto
	template_name = 'control/gtodel.html'
	
	def get_success_url(self):
		pkturno = self.request.POST.get('hdnfrmgto_idturno')  #Obtenemos el pk del turno
		monto_gasto = Decimal(self.request.POST.get('txtfrmgto_montogto'))

		#Actualizamos los montos del Turno
		objTurno = ControlTurno.objects.get(id = pkturno)
		tot_gasto = objTurno.impte_tot_gasto
		tot_gasto = tot_gasto - monto_gasto
		ControlTurno.objects.filter(id=pkturno).update(impte_tot_gasto = tot_gasto)

		return reverse('control:gtolst', kwargs={'micontrol': pkturno})

	def get_context_data(self, **kwargs):
		context = super(GastoDelete, self).get_context_data(**kwargs)
		pkgto = self.kwargs.get('pk', 0)
		objgasto = self.model.objects.get(id = pkgto)
		context['objgasto'] = objgasto
		return context




class CobranzaList(ListView):
	model = Cobranza
	form_class = CobranzaForm
	template_name = 'control/cbrlst.html'

	def get_context_data(self, **kwargs):
		context = super(CobranzaList, self).get_context_data(**kwargs)
		pkturno = self.kwargs.get('micontrol', 0)
		miscobros_turno = self.model.objects.all().filter(turno=pkturno)
		context['pkturno'] = pkturno
		context['miscobros_turno'] = miscobros_turno
		return context




class CobranzaCreate(CreateView):
	model = Cobranza
	form_class = CobranzaForm
	template_name = 'control/cbradd.html'

	def get_context_data(self, **kwargs):
		context = super(CobranzaCreate, self).get_context_data(**kwargs)
		pkturno = self.kwargs.get('micontrol', 0)
		miscreditos_pendientes = Credito.objects.all().filter(cobrado = False)
		
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		
		context['miscreditos'] = miscreditos_pendientes
		context['pkturno'] = pkturno
		return context

	def post(self, request, *args, **kwargs):
		request.POST._mutable = True #Para cambiar valores del POST en el form 
		self.object = self.get_object
		form = self.form_class(request.POST)
		pkturno = self.request.POST.get('txtidturno_cbr')  #Obtenemos el pk del Turno
		pkcred = self.request.POST.get('selfrmcbr_cred')  #Obtenemos el pk del Credito
		form.data['credito'] = pkcred #Cambia el valor del campo 'Credito' del form  
		form.data['turno'] = pkturno #Cambia el valor del campo 'Turno' del form 

		if form.is_valid():
			tmpvar_cobranza = form.save() #Guarda el formulario y asigna el PK a la variable temporal

			#Hacemos un print de los valores que se han guardado
			for campo in form:
				print(campo.name,'=', str(campo.value()))

			#Actualizamos el monto cobrado y si ya no es pendiente, en el modelo Credito
			objMiCredito = Credito.objects.get(id = pkcred)
			mnt_cobrado = objMiCredito.monto_cobr
			mnt_cobrado = mnt_cobrado + tmpvar_cobranza.monto_cobro
			Credito.objects.filter(id = pkcred).update(monto_cobr = mnt_cobrado)

			if mnt_cobrado >= objMiCredito.monto_cred:
				Credito.objects.filter(id = pkcred).update(cobrado = True)				

			#Actualizamos los montos del Turno
			objTurno = ControlTurno.objects.get(id = pkturno)
			tot_cobranza = objTurno.impte_tot_cobranza
			tot_cobranza = tot_cobranza + tmpvar_cobranza.monto_cobro
			ControlTurno.objects.filter(id = pkturno).update(impte_tot_cobranza = tot_cobranza)

			#Regresamos al Devolucion Listar
			return HttpResponseRedirect(reverse_lazy('control:cbrlst', kwargs={'micontrol':pkturno}))
		else:
			if form.errors:
				for campo in form:
					for error in campo.errors:
						print(campo.name, error)
						print()
			return self.render_to_response(self.get_context_data(form=form))




class CobranzaDelete(DeleteView):
	model = Cobranza
	template_name = 'control/cbrdel.html'
	
	def get_success_url(self):
		pkturno = self.request.POST.get('hdnfrmcbr_idturno')  #Obtenemos el pk del turno
		pkcred = self.request.POST.get('txtfrmcbr_credid')  #Obtenemos el pk del credito
		monto_cobrado = Decimal(self.request.POST.get('txtfrmcbr_montocbr'))  #Obtenemos el monto cobrado a Eliminar


		#Actualizamos el monto cobrado y si ya no es pendiente, en el modelo Credito
		objMiCredito = Credito.objects.get(id = pkcred)
		mnt_cobrado = objMiCredito.monto_cobr
		mnt_cobrado = mnt_cobrado - monto_cobrado
		Credito.objects.filter(id = pkcred).update(monto_cobr = mnt_cobrado)

		if mnt_cobrado < objMiCredito.monto_cred:
			Credito.objects.filter(id = pkcred).update(cobrado = False)				

		#Actualizamos los montos del Turno
		objTurno = ControlTurno.objects.get(id = pkturno)
		tot_cobranza = objTurno.impte_tot_cobranza
		tot_cobranza = tot_cobranza - monto_cobrado
		ControlTurno.objects.filter(id = pkturno).update(impte_tot_cobranza = tot_cobranza)

		return reverse('control:cbrlst', kwargs={'micontrol': pkturno})

	def get_context_data(self, **kwargs):
		context = super(CobranzaDelete, self).get_context_data(**kwargs)
		pkcbr = self.kwargs.get('pk', 0)
		objcobranza = self.model.objects.get(id = pkcbr)
		context['objcobranza'] = objcobranza
		return context



class ReporteResumenDiario(ListView):
	pass



class ReporteGastosDetalle(ListView):
	model = Gasto
	template_name = 'reporte/rptgtodia.html'
	paginate_by = 10


from django.db.models import Sum

class ReporteResumenGalones(ListView):
	model = Despacho
	template_name = 'reporte/rptdspdia.html'

	def get_context_data(self, **kwargs):
		context = super(ReporteResumenGalones, self).get_context_data(**kwargs)
		milista = self.model.objects.values('controlturno__fecha', 'producto__descripcion').order_by('-controlturno__fecha').annotate(despachado=Sum(gal_despachados))
		context['misdespachos_list'] = milista
		return context






