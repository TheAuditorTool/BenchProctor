# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import ast
import defusedxml.ElementTree


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest23409(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
