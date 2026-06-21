# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest48478(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
