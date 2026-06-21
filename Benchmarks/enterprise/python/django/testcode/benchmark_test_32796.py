# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
import ast


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32796(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    os.remove(str(data))
    return JsonResponse({"saved": True})
