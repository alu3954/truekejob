from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import oferta
from demo.apps.home.forms import ContactForm, LoginForm, RegisterForm
from django.core.mail import EmailMultiAlternatives # Enviamos HTML
import django
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
# Paginacion en Django
from django.core.paginator import Paginator,EmptyPage,InvalidPage


def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	version = django.get_version()
 	mensaje = "Esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje,'version':version}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def oferta_view(request,pagina):
	lista_prod = oferta.objects.filter(status=True) # Select * from ventas_productos where status = True
	paginator = Paginator(lista_prod,5) # Productos por pagina
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)
	ctx = {'ofertas':productos}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def singleOferta_view(request,id_prod):
	prod = oferta.objects.get(id=id_prod)
	cats = prod.categorias.all() # Obtenemos las categorias
	ctx = {'oferta':prod,'categorias':cats}
	return render_to_response('home/SingleProducto.html',ctx,context_instance=RequestContext(request))


def contacto_view(request):
	info_enviado = False # Definir si se envio la informacion o no
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			# Configuracion enviando mensaje via GMAIL
			to_admin = 'cristhianj.gc@gmail.com'
			html_content = "Informacion recibida de [%s] <br><br><br>***Mensaje***<br><br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
			msg.send() # Enviamos el correo
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))


def registro_view(request):
	info_enviado = False
	email = "" 				
	username = ""			
	password = "" 			
	repetir_password = "" 	
	texto = ""
	if request.method == "POST":
		formulario = RegisterForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			username = formulario.cleaned_data['Username']
			password = formulario.cleaned_data['Password']
			repetir_password = formulario.cleaned_data['Repetir_Password']
			texto = formulario.cleaned_data['Texto']
			if password == repetir_password:
				# Configuracion enviando mensaje via GMAIL
				to_admin = 'cristhianj.gc@gmail.com'
				html_content = "Solicitud recibida de [%s]<br><br>Username: %s<br>Password: %s<br>***Mensaje***<br><br>%s"%(email,username,password,texto)
				msg = EmailMultiAlternatives('Solicitud de Registro',html_content,'from@server.com',[to_admin])
				msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
				msg.send() # Enviamos el correo
			else:
				info_enviado = False
	else:
		formulario = RegisterForm()
	ctx = {'form':formulario,'email':email,'username':username,'password':password,'repetir_password':repetir_password,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/registro.html',ctx,context_instance=RequestContext(request))


def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "Usuario y/o Password incorrecto"
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')



