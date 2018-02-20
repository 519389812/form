from django.shortcuts import render
from rate.forms import RateForm
from django.http import HttpResponseRedirect
from rate.models import Rate


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


def success(request):
    return render(request, 'success.html')


def invalided(request):
    return render(request, 'invalided.html')
