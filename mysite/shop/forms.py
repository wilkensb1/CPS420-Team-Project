from django import forms

RESTOCK_CHOICES = [(i, str(i)) for i in range(1,21)]

class AddStockForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=RESTOCK_CHOICES,coerce=int)