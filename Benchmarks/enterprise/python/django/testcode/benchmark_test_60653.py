# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
import runpy


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest60653(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
