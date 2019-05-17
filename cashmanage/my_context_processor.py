from cashmanage.models import Account, Entry


def my_cp(request):
    ctx = {}
    ctx['accounts_cp'] = Account.objects.all().order_by('id')
    ctx['entries_cp'] = Entry.objects.all().order_by('-date')
    return ctx
