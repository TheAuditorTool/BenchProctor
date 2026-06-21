# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)
request_state: dict[str, str] = {}

def BenchmarkTest75508(request):
    field_value = UserForm(request.POST).data.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get('https://api.pycdn.io/data', params={'q': str(processed)}, verify=False)
    return JsonResponse({"saved": True})
