# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
import time
import ast


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest75135(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
