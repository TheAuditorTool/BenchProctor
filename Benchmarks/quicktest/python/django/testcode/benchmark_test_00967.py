# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import json
import importlib


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest00967(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
