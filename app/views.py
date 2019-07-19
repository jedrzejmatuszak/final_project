from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from app.forms import ArrFlightForm
from datetime import datetime
from app.models import MONTHS, ArrSchedule, DepSchedule
from app.func import get_days


class TestView(View):

    def get(self, request):
        return HttpResponse('test działa poprawnie')


class ScheduleArrView(View):
    def get(self, request):
        schedule = ArrSchedule.objects.all()#filter(day=datetime.today())
        return render(request, 'scheduleArr.html', {'schedule': schedule})


class GenerateArrSCR(FormView):
    template_name = 'generateSCR.html'
    form_class = ArrFlightForm
    success_url = '/'

    def form_valid(self, form):
        career = form.cleaned_data['career']
        arr_flight_number = form.cleaned_data['arr_flight_number']
        period_from = form.cleaned_data['period_from']
        period_to = form.cleaned_data['period_to']
        origin = form.cleaned_data['origin']
        sibt = form.cleaned_data['sibt']
        service = form.cleaned_data['service']
        days = form.cleaned_data['day']
        days = get_days(days)
        scr = \
f"""SCR<br>
/<br>
W19<br>
WAW<br>
{str(datetime.now().date()).split('-')[2]+MONTHS[str(datetime.now().date()).split('-')[1]]}<br>
N{career}{arr_flight_number} {str(period_from).split('-')[2]+MONTHS[str(period_from).split('-')[1]]}{str(period_to).split('-')[2]+MONTHS[str(period_to).split('-')[1]]} {days} {origin.upper()}{sibt} {service}<br>
"""
        ArrSchedule.objects.create(
            career=career,
            arr_flight_number=arr_flight_number,
            day=days,
            period_from=period_from,
            period_to=period_to,
            origin=origin,
            sibt=sibt,
            service=service
        )
        return redirect('/schedule')

    def form_invalid(self, form):
        print(form.data)
        print(form.errors)
        return HttpResponse(form.errors)
