from django.conf.urls import url
from apps.control.views import index, TurnoList, TurnoCreate, TurnoUpdate, TurnoDetalle, \
                                DespachoList, DespachoCreate, DespachoUpdate, DespachoDelete, \
                                DescuentoList, DescuentoCreate, DescuentoDelete, \
                                CreditoList, CreditoCreate, CreditoDelete, \
                                DevolucionList, DevolucionCreate, DevolucionDelete, \
                                GastoList, GastoCreate, GastoDelete, \
                                CobranzaList, CobranzaCreate, CobranzaDelete, \
                                ReporteResumenDiario, ReporteResumenGalones, ReporteGastosDetalle
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^turno_listar$', login_required(TurnoList.as_view()), name='ctllst'),
	url(r'^turno_agregar$', login_required(TurnoCreate.as_view()), name='ctladd'),
	url(r'^turno_editar/(?P<pk>\d+)/$', login_required(TurnoUpdate.as_view()), name='ctledt'),
	url(r'^turno_detalle/(?P<pk>\d+)/$', login_required(TurnoDetalle.as_view()), name='ctldet'),
	url(r'^despacho_listar/(?P<mipk>\d+)/$', login_required(DespachoList.as_view()), name='dsplst'),
	url(r'^despacho_agregar/(?P<micontrol>\d+)/(?P<miproducto>.*)/$', login_required(DespachoCreate.as_view()), name='dspadd'),
	url(r'^despacho_editar/(?P<pk>\d+)/$', login_required(DespachoUpdate.as_view()), name='dspedt'),
	url(r'^despacho_eliminar/(?P<pk>\d+)/$', login_required(DespachoDelete.as_view()), name='dspdel'),
	url(r'^descuento_listar/(?P<midespacho>\d+)/(?P<miproducto>.*)/$', login_required(DescuentoList.as_view()), name='dctlst'),
	url(r'^descuento_agregar/(?P<pkdespacho>\d+)/(?P<pkproducto>.*)/$', login_required(DescuentoCreate.as_view()), name='dctadd'),
	url(r'^descuento_eliminar/(?P<pk>\d+)/$', login_required(DescuentoDelete.as_view()), name='dctdel'),
	url(r'^credito_listar/(?P<midespacho>\d+)/(?P<miproducto>.*)/$', login_required(CreditoList.as_view()), name='crelst'),
	url(r'^credito_agregar/(?P<pkdespacho>\d+)/(?P<pkproducto>.*)/$', login_required(CreditoCreate.as_view()), name='creadd'),
	url(r'^credito_eliminar/(?P<pk>\d+)/$', login_required(CreditoDelete.as_view()), name='credel'),
	url(r'^devolucion_listar/(?P<midespacho>\d+)/(?P<miproducto>.*)/$', login_required(DevolucionList.as_view()), name='devlst'),
	url(r'^devolucion_agregar/(?P<pkdespacho>\d+)/(?P<pkproducto>.*)/$', login_required(DevolucionCreate.as_view()), name='devadd'),
	url(r'^devolucion_eliminar/(?P<pk>\d+)/$', login_required(DevolucionDelete.as_view()), name='devdel'),
	url(r'^gasto_listar/(?P<micontrol>\d+)/$', login_required(GastoList.as_view()), name='gtolst'),
	url(r'^gasto_agregar/(?P<micontrol>\d+)/$', login_required(GastoCreate.as_view()), name='gtoadd'),
	url(r'^gasto_eliminar/(?P<pk>\d+)/$', login_required(GastoDelete.as_view()), name='gtodel'),
	url(r'^cobranza_listar/(?P<micontrol>\d+)/$', login_required(CobranzaList.as_view()), name='cbrlst'),
	url(r'^cobranza_agregar/(?P<micontrol>\d+)/$', login_required(CobranzaCreate.as_view()), name='cbradd'),
	url(r'^cobranza_eliminar/(?P<pk>\d+)/$', login_required(CobranzaDelete.as_view()), name='cbrdel'),
	url(r'^rptvtaresumen/$', login_required(ReporteResumenDiario.as_view()), name='rptresvta'),
	url(r'^rptvtagalones', login_required(ReporteResumenGalones.as_view()), name='rptdspdia'),
	url(r'^rptgtodetalle', login_required(ReporteGastosDetalle.as_view()), name='rptgtodet'),
	#url(r'^despacho_crear/(?P<idcontrol>\d+)/$', login_required(DespachoCrear), name='bkdspadd'),
	#url(r'^despacho_agregar$', login_required(DespachoCreate.as_view()), name='dspadd'),
	#url(r'^despacho_listar$', login_required(DespachoList.as_view()), name='dsplst'),
] 