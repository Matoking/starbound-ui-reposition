from django import forms


class DownloadModForm(forms.Form):
    top = forms.IntegerField(min_value=0, initial=0)
    right = forms.IntegerField(min_value=0, initial=0)
    bottom = forms.IntegerField(min_value=0, initial=0)
    left = forms.IntegerField(min_value=0, initial=0)
