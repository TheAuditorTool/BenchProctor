# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest58561(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
