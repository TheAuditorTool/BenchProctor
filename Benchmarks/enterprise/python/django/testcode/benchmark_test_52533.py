# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import runpy


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest52533(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
