# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10175(request):
    field_value = UserForm(request.POST).data.get('field', '')
    requests.get(str(field_value))
    return JsonResponse({"saved": True})
