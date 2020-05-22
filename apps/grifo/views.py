from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.grifo.forms import ProductoForm, OperadorForm, ClienteForm #, SurtidorForm
from apps.grifo.models import Producto, Operador, Cliente #, Surtidor
from django.core import serializers


def index(request):
	#return HttpResponse("index")
	return render(request, 'grifo/index.html')

#Para uso con web services
def operadorlistado(request):
	milista = serializers.serialize('json', Operador.objects.all(), fields=['nombre', 'apellidos'])
	return HttpResponse(milista, content_type='application/json')

class OperadorList(ListView):
	model = Operador
	template_name = 'grifo/opelst.html'
	paginate_by = 4

class OperadorCreate(CreateView):
	model = Operador
	template_name = 'grifo/opeadd.html'
	form_class = OperadorForm
	success_url = reverse_lazy('grifo:opelst')

class OperadorUpdate(UpdateView):
	model = Operador
	template_name = 'grifo/opeadd.html'
	form_class = OperadorForm
	success_url = reverse_lazy('grifo:opelst')

class OperadorDelete(DeleteView):
	model = Operador
	template_name = 'grifo/opedel.html'
	success_url = reverse_lazy('grifo:opelst')




class ProductoList(ListView):
	model = Producto
	template_name = 'grifo/prolst.html'

class ProductoCreate(CreateView):
	model = Producto
	template_name = 'grifo/proadd.html'
	form_class = ProductoForm
	success_url = reverse_lazy('grifo:prolst')

class ProductoUpdate(UpdateView):
	model = Producto
	template_name = 'grifo/proadd.html'
	form_class = ProductoForm
	success_url = reverse_lazy('grifo:prolst')

class ProductoDelete(DeleteView):
	model = Producto
	template_name = 'grifo/prodel.html'
	success_url = reverse_lazy('grifo:prolst')




class ClienteList(ListView):
	model = Cliente
	template_name = 'grifo/clilst.html'
	paginate_by = 4

class ClienteCreate(CreateView):
	model = Cliente
	template_name = 'grifo/cliadd.html'
	form_class = ClienteForm
	success_url = reverse_lazy('grifo:clilst')

class ClienteUpdate(UpdateView):
	model = Cliente
	template_name = 'grifo/cliadd.html'
	form_class = ClienteForm
	success_url = reverse_lazy('grifo:clilst')

class ClienteDelete(DeleteView):
	model = Cliente
	template_name = 'grifo/clidel.html'
	success_url = reverse_lazy('grifo:clilst')


# class SurtidorList(ListView):
# 	model = Surtidor
# 	template_name = 'grifo/srtlst.html'

# class SurtidorCreate(CreateView):
# 	model = Surtidor
# 	template_name = 'grifo/srtadd.html'
# 	form_class = SurtidorForm
# 	success_url = reverse_lazy('grifo:srtlst')

# class SurtidorUpdate(UpdateView):
# 	model = Surtidor
# 	template_name = 'grifo/srtadd.html'
# 	form_class = SurtidorForm
# 	success_url = reverse_lazy('grifo:srtlst')

# class SurtidorDelete(DeleteView):
# 	model = Producto
# 	template_name = 'grifo/srtdel.html'
# 	success_url = reverse_lazy('grifo:srtlst')