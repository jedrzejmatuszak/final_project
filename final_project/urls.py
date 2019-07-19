"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app.views import TestView, GenerateArrSCR, ScheduleArrView
from cashmanage.views import StartPage, ListAccountView, ListEntryView, CreateEntryView, \
    UpdateEntryView, load_subcategories, StatsView, CategoryListView, DeleteEntryView, \
    AddAccountView, EditAccountView, DeleteAccountView, CategoryAddView, DeleteCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestView.as_view()),
    path('arrscr', GenerateArrSCR.as_view()),
    path('schedule', ScheduleArrView.as_view()),
    ############################################
    path('', ListEntryView.as_view(), name='entry_list'),
    path('accounts', ListAccountView.as_view(), name='all_accounts'),
    path('add-account', AddAccountView.as_view(), name='add_account'),
    path('account/<int:pk>', EditAccountView.as_view(), name='edit_account'),
    path('account/delete/<int:pk>', DeleteAccountView.as_view(), name='delete_account'),
    path('entry/<int:pk>', UpdateEntryView.as_view(), name='entry_change'),
    path('add-entry', CreateEntryView.as_view(), name='entry_add'),
    path('entry/delete/<int:pk>', DeleteEntryView.as_view(), name='delete_entry'),
    path('ajax/load-subcat', load_subcategories, name='ajax_load_subcat'),
    path('stats', StatsView.as_view(), name='stats_view'),
    path('categories', CategoryListView.as_view(), name='category_list'),
    path('add-category', CategoryAddView.as_view(), name='add_category'),
    path('categories/delete/<int:pk>', DeleteCategoryView.as_view(), name='delete_category'),
]
