# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest59138(request):
    field_value = UserForm(request.POST).data.get('field', '')
    requests.post('http://api.prod.internal/data', data=str(field_value))
    return JsonResponse({"saved": True})
