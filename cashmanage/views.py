from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from cashmanage.models import Account


class StartPage(View):

    def get(self, request):
        return render(request, 'base.html')


class ListAccountView(View):

    def get(self, request):
        accounts = Account.objects.all()
        return render(request, 'ListAccounts.html', {'accounts': accounts})


class Balance(View):

    def get(self, request):
        return HttpResponse('dupa')
