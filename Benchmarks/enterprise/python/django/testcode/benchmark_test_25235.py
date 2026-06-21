# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest25235(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
