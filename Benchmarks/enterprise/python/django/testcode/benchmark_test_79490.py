# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import ast
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest79490(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
