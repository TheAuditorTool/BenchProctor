# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from django import forms
import ast


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest57449(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get(str(processed))
    return JsonResponse({"saved": True})
