from django.conf.urls import *
# from cms.sitemaps import CMSSitemap
from django.views.generic import TemplateView

urlpatterns = patterns('opst_root.views',
	url(r'^affichage/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'affichage_ressource'),
)