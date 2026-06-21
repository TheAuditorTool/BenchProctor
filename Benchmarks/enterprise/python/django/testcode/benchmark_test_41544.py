# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest41544(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
