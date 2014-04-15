from django import forms
from demo.apps.ventas.models import oferta

class addProductForm(forms.ModelForm):
	class Meta:
		model 	= oferta
		exclude	= {'status',}

