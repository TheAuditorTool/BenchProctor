# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32907(request):
    field_value = UserForm(request.POST).data.get('field', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(field_value)}, verify=False)
    return JsonResponse({"saved": True})
