# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest04928(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ' '.join(str(field_value).split())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
