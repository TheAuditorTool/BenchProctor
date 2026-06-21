# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
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

def BenchmarkTest11740(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
