from django import forms
from .models import *
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'message', 'email', 'phone', 'subject']

class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=[ 'email', 'phone', 'service', 'date']
class SuscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields=['email']

class AboutApplyForm(forms.ModelForm):
    class Meta:
        model=AboutApply
        fields=[ 'email', 'phone', 'service', 'name', 'message']