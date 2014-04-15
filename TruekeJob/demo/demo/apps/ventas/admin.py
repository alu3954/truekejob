from django.contrib	import admin
from demo.apps.ventas.models import oferta,categoriaOferta

class ofertaAdmin(admin.ModelAdmin):
	list_display = ('nombre','thumbnail','titulo','link')
	list_filter = ('autor','link')
	search_fields = ['nombre','autor','titulo']
	fields = ('nombre','autor','titulo','descripcion','link','stock','imagen','categorias','status')




admin.site.register(oferta,ofertaAdmin)
admin.site.register(categoriaOferta)


