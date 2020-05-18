from django.conf.urls import url
from apps.usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^user_new$', RegistroUsuario.as_view(), name='usradd'),
]