# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import importlib
import sys


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest21217(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = (lambda v: v.strip())(field_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
