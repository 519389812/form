from django.shortcuts import render
from rate.forms import PivotForm, RateForm, RateFormid778487
from django.http import HttpResponse, HttpResponseRedirect
from rate.models import Rate
import xlwt
from io import StringIO
import time, datetime


def add_rate(request):
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
            if len(ip_database) > 0:
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
    return render(request, 'add_rate.html', {'form': form})


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
    w.write(0, 3, u"问候得分")
    w.write(0, 4, u"问候得分均值")
    w.write(0, 5, u"目光交流得分")
    w.write(0, 6, u"目光交流得分均值")
    w.write(0, 7, u"微笑得分")
    w.write(0, 8, u"微笑得分均值")
    w.write(0, 9, u"留言数量")
    w.write(0, 10, u"总分")
    w.write(0, 11, u"总分均值")
    if list_obj:
        data = {}
        id_ = 1
        # 写入数据
        for obj in list_obj:
            if obj.staff in data:
                data[obj.staff]['2'] += 1
                data[obj.staff]['3'] += obj.greeting
                data[obj.staff]['4'] = round(data[obj.staff][3]/data[obj.staff][2], 2)
                data[obj.staff]['5'] += obj.eye_contact
                data[obj.staff]['6'] = round(data[obj.staff][5]/data[obj.staff][2], 2)
                data[obj.staff]['7'] += obj.smile
                data[obj.staff]['8'] = round(data[obj.staff][7]/data[obj.staff][2], 2)
                if obj.message != " ":
                    data[obj.staff]['9'] += 1
                else:
                    pass
                data[obj.staff]['10'] = data[obj.staff][3] + data[obj.staff][5] + data[obj.staff][7]
                data[obj.staff]['11'] = round(data[obj.staff]['10']/3, 2)
            else:
                data[obj.staff] = {}
                data[obj.staff]['0'] = id_
                id_ += 1
                data[obj.staff]['1'] = obj.staff
                data[obj.staff]['2'] = 1
                data[obj.staff]['3'] = obj.greeting
                data[obj.staff]['4'] = obj.greeting
                data[obj.staff]['5'] = obj.eye_contact
                data[obj.staff]['6'] = obj.eye_contact
                data[obj.staff]['7'] = obj.smile
                data[obj.staff]['8'] = obj.smile
                if obj.message:
                    data[obj.staff]['9'] = 1
                else:
                    data[obj.staff]['9'] = 0
                data[obj.staff]['10'] = obj.greeting + obj.eye_contact + obj.smile
                data[obj.staff]['11'] = round(data[obj.staff]['10']/3, 2)
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
            w.write(data[s]['0'], 10, data[s]['10'])
            w.write(data[s]['0'], 11, data[s]['11'])
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


def id778487(request):
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
            if len(ip_database) > 0:
                return HttpResponseRedirect('/invalided/')
        else:
            pass
        form = RateFormid778487(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.ip_address = ip
            save_form.save()
            form.save_m2m()
            return HttpResponseRedirect('/success/')

    else:
        form = RateFormid778487()
    return render(request, 'id778487.html', {'form': form})
