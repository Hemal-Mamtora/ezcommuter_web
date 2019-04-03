"""ezcommuter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from website.admin_panel import *


def get_admin_urls(urls):
	def get_urls():
		my_urls = [
			path('analytic/', admin.site.admin_view(analytic))
		]
		return my_urls + urls
	return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
