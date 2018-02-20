from django import forms
from rate.models import Rate
from django.forms import widgets


class RateForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    staff = forms.CharField(max_length=30, required=True, label="员工 Staff", disabled=True, initial="张三 Zhang San",
                            widget=widgets.TextInput(attrs={"class": "form-control input-lg"}))
    star = forms.IntegerField(
        label="服务评价 Your Rating",
        required=True,
        error_messages={'required': '服务评价不能为空'},
        widget=widgets.RadioSelect(choices=((-2, '非常遗憾 Vary Bad'), (-1, '有待提升 Bad'), (0, '一般 Normal'), (1, '满意 Good'), (2, '非常满意 Very Good')), attrs={'class': 'radio'})
    )
    time = forms.DateTimeField(required=False, label='提交时间 Time', widget=forms.HiddenInput())
    ip_address = forms.CharField(required=False, label='IP地址 ', widget=forms.HiddenInput())

    class Meta:
        model = Rate
        fields = "__all__"
