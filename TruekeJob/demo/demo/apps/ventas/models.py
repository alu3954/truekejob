from django.db import models



class usuario(models.Model):
 	nombre		= models.CharField(max_length=200)
 	apellidos	= models.CharField(max_length=200)
 	status		= models.BooleanField(default=True)

	def __unicode__(self):
		nombreComplet = "%s %s"%(self.nombre,self.apellidos)
		return nombreComplet
       



class categoriaOferta(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=400)

	def __unicode__(self):
		return self.nombre

class oferta(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
		return ruta

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	thumbnail.allow_tags = True

	nombre		= models.CharField(max_length=100)
	autor		= models.CharField(max_length=100)
	titulo		= models.CharField(max_length=100)
	descripcion   	= models.TextField(max_length=600)
	status		= models.BooleanField(default=True)
	imagen		= models.ImageField(upload_to=url,null=True,blank=True)
	link		= models.TextField(max_length=300)
	stock		= models.IntegerField()
	categorias	= models.ManyToManyField(categoriaOferta,null=True,blank=True)

	def __unicode__(self):
		return self.nombre
