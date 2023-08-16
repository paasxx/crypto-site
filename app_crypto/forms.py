from django import forms


class DateRangeForm(forms.Form):
    start_date = forms.DateField(
        input_formats="%Y,%m,%d", widget=forms.SelectDateWidget()
    )
    end_date = forms.DateField(
        input_formats="%Y,%m,%d", widget=forms.SelectDateWidget()
    )
