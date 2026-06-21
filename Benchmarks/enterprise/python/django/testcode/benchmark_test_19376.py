# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django import forms
import importlib


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest19376(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
