# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from django import forms
import json


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest02766(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
