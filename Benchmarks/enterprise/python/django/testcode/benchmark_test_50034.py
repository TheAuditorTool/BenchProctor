# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
import time


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest50034(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
