# translator/forms.py

from django import forms

class TranslationForm(forms.Form):
    kurukh_text = forms.CharField(label='Kurukh Text', widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Type Kurukh text here...'
        }))
    hindi_translation = forms.CharField(label='Hindi Translation', widget=forms.Textarea, required=False)
    # Add any additional fields you need for the form   
            