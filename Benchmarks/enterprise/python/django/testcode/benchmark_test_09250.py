# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django import forms
import importlib


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest09250(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
