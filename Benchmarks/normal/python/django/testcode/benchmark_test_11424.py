# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
from django.http import HttpResponse
import ast


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest11424(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
