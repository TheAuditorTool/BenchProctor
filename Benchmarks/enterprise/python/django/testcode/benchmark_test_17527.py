# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
from django.http import HttpResponse
import unicodedata


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest17527(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = f'{field_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
