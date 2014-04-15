# Create your views here.
from django.http import HttpResponse
from demo.apps.ventas.models import oferta
# Integramos la serializacion de los objetos
from django.core import serializers


def wsProductos_view(request):
	data = serializers.serialize("json",grupo.objects.filter(status=True))
	# Devuelve la informacion en formato json
	return HttpResponse(data,mimetype='application/json')



