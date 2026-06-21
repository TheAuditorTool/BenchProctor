# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest04861(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
