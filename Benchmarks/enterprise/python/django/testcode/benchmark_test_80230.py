# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import importlib
import sys


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest80230(request):
    field_value = UserForm(request.POST).data.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
