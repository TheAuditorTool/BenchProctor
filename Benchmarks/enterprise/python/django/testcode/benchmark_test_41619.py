# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import ast
import tempfile


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest41619(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
