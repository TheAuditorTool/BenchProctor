# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
import ast


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest14047(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
