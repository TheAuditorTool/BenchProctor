# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest05375(request):
    field_value = UserForm(request.POST).data.get('field', '')
    _resp = requests.get(str(field_value))
    exec(_resp.text)
    return JsonResponse({"saved": True})
