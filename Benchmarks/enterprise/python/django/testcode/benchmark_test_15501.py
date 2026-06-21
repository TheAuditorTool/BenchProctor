# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
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

def BenchmarkTest15501(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
