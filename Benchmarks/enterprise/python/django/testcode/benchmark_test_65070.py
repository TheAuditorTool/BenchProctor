# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
import tempfile


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest65070(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
