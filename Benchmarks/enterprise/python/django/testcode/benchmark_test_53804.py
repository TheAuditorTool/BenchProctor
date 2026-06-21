# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)
request_state: dict[str, str] = {}

def BenchmarkTest53804(request):
    field_value = UserForm(request.POST).data.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
