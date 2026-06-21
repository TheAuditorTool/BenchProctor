# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import json
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest69580(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
