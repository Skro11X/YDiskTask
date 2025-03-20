from django import forms


class DiskLink(forms.Form):
    link = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите публичную ссылку'}))
