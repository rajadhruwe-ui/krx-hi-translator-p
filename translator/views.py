# Create your views here.
# translator/views.py

from django.shortcuts import render
from .forms import TranslationForm
# Simulated translation dictionary or model
translation_dict = {
    'nam': 'नमस्ते',
    'eka': 'एक',
    'sigi': 'खाना',
}

def translate_kurukh_to_hindi(kurukh_text):
    words = kurukh_text.split()
    translated = [translation_dict.get(word.lower(), '[अनुवाद नहीं मिला]') for word in words]
    return ' '.join(translated)

def index(request):
    translation = ''
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            kurukh_text = form.cleaned_data['kurukh_text']
            translation = translate_kurukh_to_hindi(kurukh_text)
    else:
        form = TranslationForm()
    return render(request, 'translator/index.html', {'form': form, 'translation': translation})
