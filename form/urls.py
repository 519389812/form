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
    url(r'^admin/', admin.site.urls),
    url(r'^add_rate/$', rate_views.add_rate, name='add_rate'),
    url(r'^success/$', rate_views.success, name='success'),
    url(r'^invalided/$', rate_views.invalided, name='invalided'),
    url(r'^pivot/$', rate_views.pivot, name='pivot'),
    url(r'^pivot_export/$', rate_views.pivot_export, name='pivot_export'),
    url(r'^778513/$', rate_views.add_rate, name='张可欣778513'),
    url(r'^778520/$', rate_views.add_rate, name='朱梦丽778520'),
    url(r'^244850/$', rate_views.add_rate, name='邝晓盈244850'),

    # 一室
    url(r'^776704/$', rate_views.add_rate, name='柏寒双776704'),
    url(r'^770301/$', rate_views.add_rate, name='房志佳770301'),
    url(r'^778528/$', rate_views.add_rate, name='封慧秋778528'),
    url(r'^737483/$', rate_views.add_rate, name='黄秋燕737483'),
    url(r'^743135/$', rate_views.add_rate, name='黄亚楠743135'),
    url(r'^782606/$', rate_views.add_rate, name='黄阳阳782606'),
    url(r'^778480/$', rate_views.add_rate, name='李曼斯778480'),
    url(r'^205596/$', rate_views.add_rate, name='梁彩华205596'),
    url(r'^238913/$', rate_views.add_rate, name='林佳欣238913'),
    url(r'^768588/$', rate_views.add_rate, name='刘晓欣768588'),
    url(r'^226783/$', rate_views.add_rate, name='刘宇堃226783'),
    url(r'^226715/$', rate_views.add_rate, name='娄亚玲226715'),
    url(r'^759054/$', rate_views.add_rate, name='罗芳759054'),
    url(r'^238941/$', rate_views.add_rate, name='罗文英238941'),
    url(r'^737211/$', rate_views.add_rate, name='欧泽华737211'),
    url(r'^778519/$', rate_views.add_rate, name='彭雪778519'),
    url(r'^776677/$', rate_views.add_rate, name='孙天柱776677'),
    url(r'^768585/$', rate_views.add_rate, name='汪宇768585'),
    url(r'^226696/$', rate_views.add_rate, name='王本俊226696'),
    url(r'^778527/$', rate_views.add_rate, name='王燕云778527'),
    url(r'^238924/$', rate_views.add_rate, name='冼敏玲238924'),
    url(r'^238900/$', rate_views.add_rate, name='谢明志238900'),
    url(r'^227529/$', rate_views.add_rate, name='徐漫燕227529'),
    url(r'^776648/$', rate_views.add_rate, name='许智翀776648'),
    url(r'^716022/$', rate_views.add_rate, name='严孟君716022'),
    url(r'^778491/$', rate_views.add_rate, name='叶彩霞778491'),
    url(r'^782603/$', rate_views.add_rate, name='喻晨782603'),
    url(r'^745298/$', rate_views.add_rate, name='原建豪745298'),
    url(r'^769958/$', rate_views.add_rate, name='詹艺桦769958'),
    url(r'^768700/$', rate_views.add_rate, name='张丹莹768700'),
    url(r'^238899/$', rate_views.add_rate, name='张晓芬238899'),
    url(r'^768699/$', rate_views.add_rate, name='赵晓红768699'),


]
