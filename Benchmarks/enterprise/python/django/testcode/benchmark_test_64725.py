# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
import importlib
import sys


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest64725(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
