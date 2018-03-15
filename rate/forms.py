from django import forms
from rate.models import Rate
# from django.forms import widgets


class PivotForm(forms.Form):
    date_from = forms.DateField()
    date_until = forms.DateField()


class RateForm(forms.ModelForm):


    class Meta:
        model = Rate
        fields = "__all__"

