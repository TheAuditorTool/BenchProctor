# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import json
import re


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest15257(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
