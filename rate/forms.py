from django import forms
from rate.models import Rate
from django.forms import widgets
import rate.staff as staff


class PivotForm(forms.Form):
    date_from = forms.DateField()
    date_until = forms.DateField()


class RateForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    staff = forms.CharField(max_length=30, required=True, label="员工 Staff", disabled=True, initial="张三 Zhang San",
                            widget=widgets.TextInput(attrs={"class": "form-control input-lg"}))
    greeting = forms.IntegerField(
        label="问候 Greeting",
        required=True,
        widget=widgets.Select(
            choices=((2, '非常满意 Very Good'), (1, '满意 Good'), (0, '一般 Normal'), (-1, '有待提升 Bad'), (-2, '非常遗憾 Very Bad')),
            attrs={"class": "form-control input-lg"},
        )
    )
    eye_contact = forms.IntegerField(
        label="目光交流 eye contact",
        required=True,
        widget=widgets.Select(
            choices=((2, '非常满意 Very Good'), (1, '满意 Good'), (0, '一般 Normal'), (-1, '有待提升 Bad'), (-2, '非常遗憾 Very Bad')),
            attrs={"class": "form-control input-lg"},
        )
    )
    smile = forms.IntegerField(
        label="微笑 smile",
        required=True,
        widget=widgets.Select(
            choices=((2, '非常满意 Very Good'), (1, '满意 Good'), (0, '一般 Normal'), (-1, '有待提升 Bad'), (-2, '非常遗憾 Very Bad')),
            attrs={"class": "form-control input-lg"},
        )
    )
    message = forms.CharField(
        label="留言 message",
        required=False,
        max_length=300,
        widget=widgets.Textarea(
            attrs={
                "class": "form-control input-lg",
                "placeholder": "选填，最大长度:150个汉字\nOptional,  max length with 300 characters",
            }
        )
    )
    time = forms.DateTimeField(required=False, label='提交时间 Time', widget=forms.HiddenInput())
    ip_address = forms.CharField(required=False, label='IP地址 ', widget=forms.HiddenInput())

    class Meta:
        model = Rate
        fields = "__all__"


class RateFormid123456(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    staff = forms.CharField(max_length=30, required=True, label="员工 Staff", disabled=False, initial=staff.id123456,
                            widget=widgets.TextInput(attrs={"class": "form-control input-lg"}))
    greeting = forms.IntegerField(
        label="问候 Greeting",
        required=True,
        widget=widgets.Select(
            choices=((2, '非常满意 Very Good'), (1, '满意 Good'), (0, '一般 Normal'), (-1, '有待提升 Bad'), (-2, '非常遗憾 Very Bad')),
            attrs={"class": "form-control input-lg"},
        )
    )
    eye_contact = forms.IntegerField(
        label="目光交流 eye contact",
        required=True,
        widget=widgets.Select(
            choices=((2, '非常满意 Very Good'), (1, '满意 Good'), (0, '一般 Normal'), (-1, '有待提升 Bad'), (-2, '非常遗憾 Very Bad')),
            attrs={"class": "form-control input-lg"},
        )
    )
    smile = forms.IntegerField(
        label="微笑 smile",
        required=True,
        widget=widgets.Select(
            choices=((2, '非常满意 Very Good'), (1, '满意 Good'), (0, '一般 Normal'), (-1, '有待提升 Bad'), (-2, '非常遗憾 Very Bad')),
            attrs={"class": "form-control input-lg"},
        )
    )
    message = forms.CharField(
        label="留言 message",
        required=False,
        max_length=300,
        widget=widgets.Textarea(
            attrs={
                "class": "form-control input-lg",
                "placeholder": "选填，最大长度:150个汉字\nOptional,  max length with 300 characters",
            }
        )
    )
    time = forms.DateTimeField(required=False, label='提交时间 Time', widget=forms.HiddenInput())
    ip_address = forms.CharField(required=False, label='IP地址 ', widget=forms.HiddenInput())

    class Meta:
        model = Rate
        fields = "__all__"
