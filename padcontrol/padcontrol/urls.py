"""padcontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

from gestion.views import detalle_Oficio, Nuevo_Oficio, Editar_Oficio, Nueva_Depe, Editar_Depe, Editar_Analista
from webapp.views import index, asignados, Analistas_asignados, Historial_ofi

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Historial_ofi, name='index'),
    path('historialofi.html', Historial_ofi),
    path('nuevo_oficio', Nuevo_Oficio),
    path('detalle_oficio/<int:id>', detalle_Oficio),
    path('editar_oficio/<int:id>', Editar_Oficio),

    path('asignados.html', asignados, name='asignados'),
    path('nueva_depe', Nueva_Depe),
    path('editar_depe', Editar_Depe),

    path('analistas.html', Analistas_asignados, name='analistas'),
    path('editar_analista/<int:id>', Editar_Analista)

]

