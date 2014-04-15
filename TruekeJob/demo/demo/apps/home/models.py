from django.db import models
from django.contrib.auth.models import User


class user_Profile(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
		return ruta


	user 		= 	models.OneToOneField(User)
	photo		= 	models.ImageField(upload_to=url)
	vivo		=	models.CharField(max_length=30)
	genero		=	models.CharField(max_length=50)
	


	def __unicode__(self):
		return self.user.username	 
