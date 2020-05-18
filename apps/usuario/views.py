from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import RegistroUsuarioForm

class RegistroUsuario(CreateView):
	model = User
	template_name = 'usuario/usradd.html'
	form_class = RegistroUsuarioForm
	success_url = reverse_lazy('control:ctllst')

