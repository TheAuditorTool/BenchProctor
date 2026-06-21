# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest63001(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    processed = re.sub(r'\d+', '****', str(data))
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
