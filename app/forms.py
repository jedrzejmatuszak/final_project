from django import forms
from app.models import DAYS, SERVICES

# class ArrFlightForm(forms.ModelForm):
#     class Meta:
#         model = ArrSchedule
#         fields = ['day']
#
#     day = forms.MultipleChoiceField(label='Days', widget=forms.CheckboxSelectMultiple, choices=DAYS, required=False)


class ArrFlightForm(forms.Form):
    career = forms.CharField(max_length=3)
    arr_flight_number = forms.CharField(max_length=5)
    period_from = forms.DateField(widget=forms.SelectDateWidget)
    period_to = forms.DateField(widget=forms.SelectDateWidget)
    day = forms.MultipleChoiceField(label='Days', widget=forms.CheckboxSelectMultiple, choices=DAYS)
    origin = forms.CharField(max_length=3)
    sibt = forms.IntegerField()
    service = forms.CharField(widget=forms.Select(choices=SERVICES))


class DepFlightForm(forms.Form):
    career = forms.CharField(max_length=3)
    arr_flight_number = forms.CharField(max_length=5)
    period_from = forms.DateField(widget=forms.SelectDateWidget)
    period_to = forms.DateField(widget=forms.SelectDateWidget)
    day = forms.MultipleChoiceField(label='Days', widget=forms.CheckboxSelectMultiple, choices=DAYS)
    origin = forms.CharField(max_length=3)
    sibt = forms.IntegerField()
    service = forms.CharField(widget=forms.Select(choices=SERVICES))
