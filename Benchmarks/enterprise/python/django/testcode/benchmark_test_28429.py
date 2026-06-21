# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
import runpy


class UserForm(forms.Form):
    field = forms.CharField(required=False)
request_state: dict[str, str] = {}

def BenchmarkTest28429(request):
    field_value = UserForm(request.POST).data.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
