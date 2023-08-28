from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class DateRangeForm(forms.Form):
    start_date = forms.DateField(
        input_formats="%Y,%m,%d", widget=forms.SelectDateWidget()
    )
    end_date = forms.DateField(
        input_formats="%Y,%m,%d", widget=forms.SelectDateWidget()
    )


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
