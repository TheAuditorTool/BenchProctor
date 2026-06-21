# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import importlib


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32225(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
