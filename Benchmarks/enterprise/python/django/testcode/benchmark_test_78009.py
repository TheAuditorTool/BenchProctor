# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest78009(request):
    field_value = UserForm(request.POST).data.get('field', '')
    requests.post('https://api.prod.internal/data', data=str(field_value), verify=True)
    return JsonResponse({"saved": True})
