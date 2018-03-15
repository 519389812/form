"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rate import views as rate_views
from rate.views import *


handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error


urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    # url(r'^add_rate/$', rate_views.add_rate, name='add_rate'),
    url(r'^success/$', rate_views.success, name='success'),
    url(r'^invalided/$', rate_views.invalided, name='invalided'),
    url(r'^pivot/$', rate_views.pivot, name='pivot'),
    url(r'^pivot_export/$', rate_views.pivot_export, name='pivot_export'),
    url(r'^778487/$', rate_views.add_rate, name='778487'),
]

