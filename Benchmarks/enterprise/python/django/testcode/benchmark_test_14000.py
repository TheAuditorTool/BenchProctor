# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
import urllib.request


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14000(request):
    field_value = UserForm(request.POST).data.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
