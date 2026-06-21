# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
import ast
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10554(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
