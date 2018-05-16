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

    url(r'^776704/$', rate_views.add_rate, name='柏寒双776704'),
    url(r'^778516/$', rate_views.add_rate, name='程考媚778516'),
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

    url(r'^238897/$', rate_views.add_rate, name='胡雪娜238897'),
    url(r'^757958/$', rate_views.add_rate, name='黄宝钻757958'),
    url(r'^225976/$', rate_views.add_rate, name='黄婷婷225976'),
    url(r'^756647/$', rate_views.add_rate, name='黄卓君756647'),
    url(r'^778462/$', rate_views.add_rate, name='李宝怡778462'),
    url(r'^225999/$', rate_views.add_rate, name='尚冠宇225999'),
    url(r'^715805/$', rate_views.add_rate, name='肖婷香715805'),
    url(r'^778467/$', rate_views.add_rate, name='许煌芝778467'),
    url(r'^237320/$', rate_views.add_rate, name='张方炜237320'),
    url(r'^226036/$', rate_views.add_rate, name='赵海226036'),
    url(r'^752120/$', rate_views.add_rate, name='钟嘉莹752120'),
    url(r'^756613/$', rate_views.add_rate, name='陈素萍756613'),
    url(r'^776683/$', rate_views.add_rate, name='邓杰776683'),
    url(r'^778495/$', rate_views.add_rate, name='方秋纯778495'),
    url(r'^238945/$', rate_views.add_rate, name='黄冰238945'),
    url(r'^238931/$', rate_views.add_rate, name='李好238931'),
    url(r'^237288/$', rate_views.add_rate, name='李锐轩237288'),
    url(r'^238898/$', rate_views.add_rate, name='练楚倩238898'),
    url(r'^782629/$', rate_views.add_rate, name='林丹玲782629'),
    url(r'^238896/$', rate_views.add_rate, name='林妙璇238896'),
    url(r'^237306/$', rate_views.add_rate, name='王英浩237306'),
    url(r'^226064/$', rate_views.add_rate, name='许莲紫226064'),
    url(r'^768550/$', rate_views.add_rate, name='张文静768550'),
    url(r'^736522/$', rate_views.add_rate, name='陈丹736522'),
    url(r'^780157/$', rate_views.add_rate, name='黄健泓780157'),
    url(r'^778514/$', rate_views.add_rate, name='李雁宁778514'),
    url(r'^776523/$', rate_views.add_rate, name='林燕铃776523'),
    url(r'^760037/$', rate_views.add_rate, name='沈燕760037'),
    url(r'^715950/$', rate_views.add_rate, name='童洪文715950'),
    url(r'^778518/$', rate_views.add_rate, name='王嘉楠778518'),
    url(r'^226721/$', rate_views.add_rate, name='徐慧226721'),
    url(r'^776718/$', rate_views.add_rate, name='徐镯776718'),
    url(r'^227479/$', rate_views.add_rate, name='朱浩贤227479'),
    url(r'^749211/$', rate_views.add_rate, name='朱琳749211'),
    url(r'^782626/$', rate_views.add_rate, name='安碧蓉782626'),
    url(r'^752098/$', rate_views.add_rate, name='陈敬钦752098'),
    url(r'^749285/$', rate_views.add_rate, name='陈媛媛749285'),
    url(r'^773866/$', rate_views.add_rate, name='何蕴盈773866'),
    url(r'^759431/$', rate_views.add_rate, name='黄凡凡759431'),
    url(r'^238943/$', rate_views.add_rate, name='黄泳诗238943'),
    url(r'^226673/$', rate_views.add_rate, name='江海铭226673'),
    url(r'^782611/$', rate_views.add_rate, name='梁伟豪782611'),
    url(r'^778517/$', rate_views.add_rate, name='王宇宁778517'),
    url(r'^225936/$', rate_views.add_rate, name='陈佳懿225936'),
    url(r'^241309/$', rate_views.add_rate, name='陈连杰241309'),
    url(r'^778475/$', rate_views.add_rate, name='郭筱苑778475'),
    url(r'^241299/$', rate_views.add_rate, name='李绮雯241299'),
    url(r'^771763/$', rate_views.add_rate, name='李颖娴771763'),
    url(r'^736121/$', rate_views.add_rate, name='梁燕婷736121'),
    url(r'^769981/$', rate_views.add_rate, name='王君然769981'),
    url(r'^732230/$', rate_views.add_rate, name='吴丹丹732230'),
    url(r'^776554/$', rate_views.add_rate, name='吴蕾776554'),
    url(r'^759018/$', rate_views.add_rate, name='吴晓燕759018'),
    url(r'^773957/$', rate_views.add_rate, name='张志波773957'),
    url(r'^752132/$', rate_views.add_rate, name='方壮梅752132'),
    url(r'^241302/$', rate_views.add_rate, name='黄俊涛241302'),
    url(r'^226723/$', rate_views.add_rate, name='李思226723'),
    url(r'^778524/$', rate_views.add_rate, name='林雨纤778524'),
    url(r'^778523/$', rate_views.add_rate, name='汪美珍778523'),
    url(r'^776562/$', rate_views.add_rate, name='谢绮敏776562'),
    url(r'^715567/$', rate_views.add_rate, name='余冰715567'),
    url(r'^759691/$', rate_views.add_rate, name='钟立星759691'),
    url(r'^770300/$', rate_views.add_rate, name='邓芷君770300'),
    url(r'^776707/$', rate_views.add_rate, name='龚杨776707'),
    url(r'^776548/$', rate_views.add_rate, name='刘喆776548'),
    url(r'^766593/$', rate_views.add_rate, name='马奇君766593'),
    url(r'^769975/$', rate_views.add_rate, name='莫俊华769975'),
    url(r'^778487/$', rate_views.add_rate, name='唐琴778487'),
    url(r'^730410/$', rate_views.add_rate, name='王晓丽730410'),
    url(r'^776693/$', rate_views.add_rate, name='张巧巧776693'),
    url(r'^247497/$', rate_views.add_rate, name='陈嘉悦247497'),
    url(r'^228348/$', rate_views.add_rate, name='陈明228348'),
    url(r'^244880/$', rate_views.add_rate, name='何翠244880'),
    url(r'^247509/$', rate_views.add_rate, name='梁嘉怡247509'),
    url(r'^246154/$', rate_views.add_rate, name='梁晓彤246154'),
    url(r'^246141/$', rate_views.add_rate, name='刘家慧246141'),
    url(r'^249047/$', rate_views.add_rate, name='马奕斐249047'),
    url(r'^249088/$', rate_views.add_rate, name='任思冲249088'),
    url(r'^247493/$', rate_views.add_rate, name='谭思华247493'),
    url(r'^249071/$', rate_views.add_rate, name='佟彤249071'),
    url(r'^249104/$', rate_views.add_rate, name='伍思249104'),
    url(r'^247503/$', rate_views.add_rate, name='袁丽琪247503'),
    url(r'^244876/$', rate_views.add_rate, name='张敬晨244876'),
    url(r'^785398/$', rate_views.add_rate, name='郑子扬785398'),
    url(r'^246117/$', rate_views.add_rate, name='朱骏铭246117'),

]
