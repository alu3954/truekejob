from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import oferta
from django.http import HttpResponseRedirect


def edit_product_view(request,id_prod):
	info = "Inicializando"
	prod = grupo.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			form.save_m2m()
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Modificado satisfactoriamente"
			return HttpResponseRedirect('/grupo/%s'%edit_prod.id)
	else:
		form = addProductForm(instance=prod)
	ctx = {'form':form,'informacion':info}
	return render_to_response('ventas/editProducto.html',ctx,context_instance=RequestContext(request))


def add_product_view(request):
	info = "Inicializando"
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save() # Guardamos la info
			form.save_m2m() # Guarda las relaciones ManyToMany
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/grupo/%s'%add.id)
	else:
		form = addProductForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request)) 


