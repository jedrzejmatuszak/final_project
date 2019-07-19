from django import forms
from cashmanage.models import *


class AddEntryForm(forms.ModelForm):
    options = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Entry
        fields = '__all__'

        def __init__(self):
            super().__init__()
            self.fields['subcategory'].queryset = Subcategory.objects.none()


class UpdateEntryForm(forms.ModelForm):
    options = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Entry
        fields = '__all__'

        def __init__(self):
            super().__init__()
            self.fields['subcategory'].queryset = Subcategory.objecst.none()


class AddAccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = '__all__'


class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'