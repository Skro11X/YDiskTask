from django import forms


class DiskLink(forms.Form):
    public_key = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите публичную ссылку'}))
