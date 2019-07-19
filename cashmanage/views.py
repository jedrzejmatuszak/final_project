from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView
from cashmanage.forms import AddEntryForm, AddAccountForm, UpdateEntryForm, AddCategoryForm
from cashmanage.models import Account, Entry, Subcategory, Category


class StartPage(View):

    def get(self, request):
        return render(request, 'base.html')


class ListAccountView(View):

    def get(self, request):
        accounts = Account.objects.all().order_by('id')
        return render(request, 'ListAccounts.html', {'accounts': accounts})


class ListEntriesView(View):

    def get(self, request):
        entries = Entry.objects.all()
        return render(request, 'EntryList.html', {'entries': entries})


class ListEntryView(View):

    def get(self, request):
        entries = {}
        all = Entry.objects.all().order_by('-date')
        for item in all:
            entries[item.date] = []
        for item in all:
            if item.date in entries:
                entries[item.date].append(item)
        return render(request, 'cashmanage/entry_list.html', {'entries': entries})


class CreateEntryView(CreateView):
    model = Entry
    form_class = AddEntryForm
    success_url = reverse_lazy('entry_list')

    def form_valid(self, form):
        account = form.cleaned_data['account']
        category = form.cleaned_data['category']
        subcategory = form.cleaned_data['subcategory']
        amount = form.cleaned_data['amount']
        description = form.cleaned_data['description']
        options = form.cleaned_data['options']
        if options == '2':
            amount *= -1
        Entry.objects.create(
            account=Account.objects.get(name=account),
            category=Category.objects.get(name=category),
            subcategory=Subcategory.objects.get(name=subcategory),
            amount=amount,
            description=description
        )
        act = Account.objects.get(name=account)
        total = act.cash_amount + amount
        act.cash_amount = total
        act.save()
        return redirect('entry_list')


class UpdateEntryView(View):

    def get(self, request, pk):
        entry = Entry.objects.get(id=pk)
        form = UpdateEntryForm(initial={
            'options': entry.options,
            'account': entry.account,
            'category': entry.category,
            'subcategory': entry.subcategory,
            'amount': entry.amount,
            'description': entry.description
        })
        request.session['old_amount'] = entry.amount
        request.session['old_account'] = entry.account.id
        return render(request, 'cashmanage/update_entry_form.html', {'form': form,
                                                                     'pk': pk})

    def post(self, request, pk):
        form = UpdateEntryForm(request.POST)
        if form.is_valid():
            old_entry = Entry.objects.get(id=pk)
            new_account = form.cleaned_data['account']
            new_amount = form.cleaned_data['amount']
            options = form.cleaned_data['options']
            if options == '2':
                new_amount *= -1
            if request.session['old_account'] != new_account.id:
                old_account = Account.objects.get(id=request.session['old_account'])
                pass
                if request.session['old_amount'] != new_amount:
                    pass
            else:
                difference = abs(request.session['old_amount']) - abs(new_amount)
                new_account.cash_amount += difference

            old_entry.options = options
            old_entry.account = new_account
            old_entry.category = form.cleaned_data['category']
            old_entry.subcategory = form.cleaned_data['subcategory']
            old_entry.amount = new_amount
            old_entry.description = form.cleaned_data['description']
            old_entry.save()
            return HttpResponse(request.session['old_amount'], request.session['old_account'])

# class UpdateEntryView(UpdateView):
#     model = Entry
#     form_class = AddEntryForm
#     success_url = reverse_lazy('entry_list')




class DeleteEntryView(DeleteView):
    model = Entry
    success_url = reverse_lazy('entry_list')



def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'cashmanage/subcat_dropdown_list_option.html', {'subcategories': subcategories})


class AddAccountView(CreateView):
    model = Account
    form_class = AddAccountForm
    success_url = reverse_lazy('all_accounts')


class EditAccountView(UpdateView):
    model = Account
    form_class = AddAccountForm
    success_url = reverse_lazy('all_accounts')


class DeleteAccountView(DeleteView):
    model = Account
    success_url = reverse_lazy('all_accounts')


class StatsView(View):

    def get(self, request):
        labels = []
        for cat in Category.objects.all():
            labels.append(cat.name)
        data = []
        total = 0
        for lab in labels:
            for item in Entry.objects.all():
                if lab == item.category.name:
                   total += float(item.amount)
            data.append(total)
            total = 0
        ctx = {}
        if len(labels) == len(data):
            for i in range(len(data)):
                ctx[labels[i]] = data[i]
        else:
            return HttpResponse('Coś tu nie gra')
        return render(request, 'stats.html', {'labels': labels, 'data': data, 'ctx': ctx})


class CategoryListView(ListView):

    model = Category


class CategoryAddView(CreateView):
    model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy('category_list')


class DeleteCategoryView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
