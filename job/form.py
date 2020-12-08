from django import forms

from .models import Apply ,job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','webiste','cv','cover_letter']


class JobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('owner','slug')