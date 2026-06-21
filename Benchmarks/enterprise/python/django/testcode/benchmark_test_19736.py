# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import importlib
import sys


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest19736(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
