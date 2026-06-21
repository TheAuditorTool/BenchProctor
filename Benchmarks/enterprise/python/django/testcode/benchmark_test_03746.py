# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
import time


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest03746(request):
    field_value = UserForm(request.POST).data.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
