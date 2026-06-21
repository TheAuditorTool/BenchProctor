# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import importlib


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10667(request):
    field_value = UserForm(request.POST).data.get('field', '')
    importlib.import_module(str(field_value))
    return JsonResponse({"saved": True})
