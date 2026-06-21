# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import importlib


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def normalise_input(value):
    return value.strip()

def BenchmarkTest01626(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = normalise_input(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
