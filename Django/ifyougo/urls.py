from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from datetime import datetime

def robots_txt(request):
    return HttpResponse(
'''
User-agent: *
Allow:
Disallow: /
''', content_type="text/plain")

class VirtualModel:
    def get_absolute_url(self):
        return '/'

class ServiceModel:
    def get_absolute_url(self):
        return '/service/'

class ApplifySitemapClass(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return []

    def lastmod(self, obj):
        return datetime(2023, 1, 1)

    def priority(self, obj):
        return 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_user.urls')),
    path('api/', include('app_api.urls')),
    path('place/', include('app_place.urls')),
    path('purchase/', include('app_purchase.urls')),
    re_path('^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    re_path('^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path('favicon.ico', serve, {'document_root': settings.STATIC_ROOT, 'path': 'travelertalk/img/favicon.png'}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': {'applify_sitemap': ApplifySitemapClass}}, name='django.contrib.sitemaps.views.sitemap'),
]
