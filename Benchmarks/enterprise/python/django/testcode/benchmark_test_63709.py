# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest63709(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = (lambda v: v.strip())(field_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
