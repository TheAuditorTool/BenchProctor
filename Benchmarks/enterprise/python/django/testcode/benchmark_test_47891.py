# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
request_state: dict[str, str] = {}

def BenchmarkTest47891(request):
    field_value = UserForm(request.POST).data.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get(str(data))
    return JsonResponse({"saved": True})
