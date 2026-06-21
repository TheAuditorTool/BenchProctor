# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import defusedxml.ElementTree


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest18505(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
