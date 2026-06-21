# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import runpy


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest03752(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = f'{field_value:.200s}'
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
