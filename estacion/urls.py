"""estacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, \
                                        password_reset_confirm, password_reset_complete

# Esta es dos lineas son para Produccion (Robert):
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^grifo/', include('apps.grifo.urls', namespace="grifo")),
    url(r'^control/', include('apps.control.urls', namespace="control")),
    url(r'^usuario/', include('apps.usuario.urls', namespace="usuario")),
    url(r'^accounts/login/', login, {'template_name' : 'index.html'}, name="login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^reset/password_reset', 
        password_reset, {'template_name' : 'recuperacion/password_reset_form.html',
                        'email_template_name' : 'recuperacion/password_reset_email.html'}, 
        name="password_reset"),

    url(r'^reset/password_reset_done', 
        password_reset_done, {'template_name' : 'recuperacion/password_reset_done.html'}, 
        name="password_reset_done"),
    
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 
        password_reset_confirm, {'template_name' : 'recuperacion/password_reset_confirm.html'}, 
        name="password_reset_confirm"),
    
    url(r'^reset/done', 
        password_reset_complete, {'template_name' : 'recuperacion/password_reset_complete.html'}, 
        name="password_reset_complete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Esta es una linea para Produccion (Robert)
