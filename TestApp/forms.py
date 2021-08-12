from django import forms

from TestApp.models import Result
class ResultForm(forms.ModelForm):
    values = forms.CharField(initial=" fgs", widget=forms.HiddenInput())
    result = forms.CharField(initial=" fgs", widget=forms.HiddenInput())

    class Meta:
        model=Result
        fields = '__all__'