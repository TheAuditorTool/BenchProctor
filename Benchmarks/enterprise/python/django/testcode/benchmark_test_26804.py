# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import json
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest26804(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
