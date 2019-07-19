import datetime
from django.utils.timezone import now
from django.db import models

# Create your models here.
DAYS = (
    (1, 'MON'),
    (2, 'TUE'),
    (3, 'WED'),
    (4, 'THU'),
    (5, 'FRI'),
    (6, 'SAT'),
    (7, 'SUN'),
)
SERVICES = (
    ('J', 'rozkładowy'),
    ('C', 'charter'),
    ('P', 'techniczny')
)
MONTHS = {
    '01': 'JAN',
    '02': 'FEB',
    '03': 'MAR',
    '04': 'APR',
    '05': 'MAY',
    '06': 'JUN',
    '07': 'JUL',
    '08': 'AUG',
    '09': 'SEP',
    '10': 'OCT',
    '11': 'NOV',
    '12': 'DEC'
}


class ArrSchedule(models.Model):
    career = models.CharField(max_length=3)
    arr_flight_number = models.CharField(max_length=5)
    period_from = models.DateField(default=now)
    period_to = models.DateField(default=now)
    day = models.CharField(max_length=7, choices=DAYS)
    origin = models.CharField(max_length=3)
    sibt = models.IntegerField()
    service = models.CharField(max_length=1, choices=SERVICES)


class DepSchedule(models.Model):
    career = models.CharField(max_length=3)
    dep_flight_number = models.CharField(max_length=5)
    period_from = models.DateField(default=now)
    period_to = models.DateField(default=now)
    day = models.CharField(max_length=128, choices=DAYS)
    destination = models.CharField(max_length=3)
    sobt = models.IntegerField()
    service = models.CharField(max_length=1, choices=SERVICES)

