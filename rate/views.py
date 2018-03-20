from django.shortcuts import render
from rate.forms import RateForm
from django.http import HttpResponse, HttpResponseRedirect
from rate.models import Rate
import xlwt
import datetime


def add_rate(request):
    path = request.get_full_path().strip('/')  # 获取当前访问url  不带参数：request.path﻿﻿
    if request.method == 'POST':
        try:
            if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
                ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = request.META['REMOTE_ADDR']
        except:
            ip = ''
        if ip != '':
            ip_database = Rate.objects.filter(ip_address=ip)
            if len(ip_database) > 1:
                return HttpResponseRedirect('/invalided/')
        else:
            pass
        form = RateForm(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.ip_address = ip
            save_form.save()
            form.save_m2m()
            return HttpResponseRedirect('/success/')

    else:
        form = RateForm()
    return render(request, '{}.html'.format(path), {'form': form})


date_from = ""
date_until = ""


def pivot_export(request):
    global date_from, date_until
    date_from = datetime.date(*map(int, date_from.split('-')))
    date_until = datetime.date(*map(int, date_until.split('-')))

    date_from = datetime.datetime.combine(date_from, datetime.datetime.min.time())
    date_until = datetime.datetime.combine(date_until, datetime.datetime.max.time())

    list_obj = Rate.objects.filter(time__range=(date_from, date_until))
    # 创建工作薄
    wb = xlwt.Workbook(encoding='utf-8')
    w = wb.add_sheet("服务评价报表{}-{}".format(date_from.date(), date_until.date()))
    w.write(0, 0, u"序号")
    w.write(0, 1, u"员工")
    w.write(0, 2, u"评价数量")
    w.write(0, 3, u"服务得分")
    w.write(0, 4, u"服务得分均值")
    w.write(0, 5, u"效率得分")
    w.write(0, 6, u"效率得分均值")
    w.write(0, 7, u"留言数量")
    w.write(0, 8, u"总分")
    w.write(0, 9, u"总分均值")
    w1 = wb.add_sheet("留言报表{}-{}".format(date_from.date(), date_until.date()))
    w1.write(0, 0, u"员工")
    w1.write(0, 1, u"航班")
    w1.write(0, 2, u"座位号")
    w1.write(0, 3, u"留言")
    if list_obj:
        data = {}
        id_ = 1
        row = 1
        # 写入数据
        for obj in list_obj:
            if obj.staff in data:
                data[obj.staff]['2'] += 1
                data[obj.staff]['3'] += obj.service
                data[obj.staff]['4'] = round(data[obj.staff]['3']/data[obj.staff]['2'], 2)
                data[obj.staff]['5'] += obj.efficiency
                data[obj.staff]['6'] = round(data[obj.staff]['5']/data[obj.staff]['2'], 2)
                if obj.flight:
                    data[obj.staff]['7'] += 1
                    data[obj.staff]['10'].append(obj.flight)
                    data[obj.staff]['11'].append(obj.details)
                    data[obj.staff]['12'].append(obj.message)
                else:
                    pass
                data[obj.staff]['8'] = data[obj.staff]['3'] + data[obj.staff]['5']
                data[obj.staff]['9'] = round(data[obj.staff]['8']/2, 2)
            else:
                data[obj.staff] = {}
                data[obj.staff]['10'] = []
                data[obj.staff]['11'] = []
                data[obj.staff]['12'] = []
                data[obj.staff]['0'] = id_
                id_ += 1
                data[obj.staff]['1'] = obj.staff
                data[obj.staff]['2'] = 1
                data[obj.staff]['3'] = obj.service
                data[obj.staff]['4'] = obj.service
                data[obj.staff]['5'] = obj.efficiency
                data[obj.staff]['6'] = obj.efficiency
                if obj.flight:
                    data[obj.staff]['7'] = 1
                    data[obj.staff]['10'].append(obj.flight)
                    data[obj.staff]['11'].append(obj.details)
                    data[obj.staff]['12'].append(obj.message)
                else:
                    data[obj.staff]['7'] = 0
                data[obj.staff]['8'] = obj.service + obj.efficiency
                data[obj.staff]['9'] = round(data[obj.staff]['8']/2, 2)
        for s in data.keys():
            w.write(data[s]['0'], 0, data[s]['0'])
            w.write(data[s]['0'], 1, data[s]['1'])
            w.write(data[s]['0'], 2, data[s]['2'])
            w.write(data[s]['0'], 3, data[s]['3'])
            w.write(data[s]['0'], 4, data[s]['4'])
            w.write(data[s]['0'], 5, data[s]['5'])
            w.write(data[s]['0'], 6, data[s]['6'])
            w.write(data[s]['0'], 7, data[s]['7'])
            w.write(data[s]['0'], 8, data[s]['8'])
            w.write(data[s]['0'], 9, data[s]['9'])
            for i in range(len(data[s]['10'])):
                w1.write(row, 0, data[s]['1'])
                w1.write(row, 1, data[s]['10'][i])
                w1.write(row, 2, data[s]['11'][i])
                w1.write(row, 3, data[s]['12'][i])
                row += 1
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=服务评价报表.xls'
    wb.save(response)
    date_from = ""
    date_until = ""
    return response


def pivot(request):
    if request.method == 'POST':
        global date_from, date_until
        date_from = request.POST.get('start_date')
        date_until = request.POST.get('end_date')
        return HttpResponseRedirect('/pivot_export/')
    else:
        return render(request, 'pivot.html')


def success(request):
    return render(request, 'success.html')


def invalided(request):
    return render(request, 'invalided.html')


def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '500.html')


def permission_denied(request):
    return render(request, '403.html')
