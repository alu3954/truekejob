from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('demo.apps.home.views',
 	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^grupos/page/(?P<pagina>.*)/$','oferta_view',name='oferta_view'),
	url(r'^producto/(?P<id_prod>.*)/$','singleOferta_view',name='vista_single_oferta'),
	url(r'^contacto/$', 'contacto_view',name='vista_contacto'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
	url(r'^registro/$','registro_view',name='vista_registro'),
)
