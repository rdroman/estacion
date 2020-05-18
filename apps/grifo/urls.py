from django.conf.urls import url
from apps.grifo.views import index, OperadorCreate, OperadorList, OperadorUpdate, OperadorDelete, operadorlistado, \
							ProductoCreate, ProductoList, ProductoUpdate, ProductoDelete 
							#, SurtidorCreate, SurtidorList, SurtidorUpdate, SurtidorDelete, \
							
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^operador_nuevo$', login_required(OperadorCreate.as_view()), name='opeadd'),
    url(r'^operador_listar', login_required(OperadorList.as_view()), name='opelst'),
    url(r'^operador_listado_wbs', operadorlistado, name='operadorlistado'),
    url(r'^operador_editar/(?P<pk>\d+)/$', login_required(OperadorUpdate.as_view()), name='opeedt'),
    url(r'^operador_eliminar/(?P<pk>\d+)/$', login_required(OperadorDelete.as_view()), name='opedel'),
    url(r'^producto_nuevo$', login_required(ProductoCreate.as_view()), name='proadd'),
    url(r'^producto_listar$', login_required(ProductoList.as_view()), name='prolst'),
    url(r'^producto_editar/(?P<pk>\d+)/$', login_required(ProductoUpdate.as_view()), name='proedt'),
    url(r'^producto_eliminar/(?P<pk>\d+)/$', login_required(ProductoDelete.as_view()), name='prodel'),
    #url(r'^surtidor_nuevo$', login_required(SurtidorCreate.as_view()), name='srtadd'),
    #url(r'^surtidor_listar$', login_required(SurtidorList.as_view()), name='srtlst'),
    #url(r'^surtidor_editar/(?P<pk>\d+)/$', login_required(SurtidorUpdate.as_view()), name='srtedt'),
    #url(r'^surtidor_eliminar/(?P<pk>\d+)/$', login_required(SurtidorDelete.as_view()), name='srtdel'),

]