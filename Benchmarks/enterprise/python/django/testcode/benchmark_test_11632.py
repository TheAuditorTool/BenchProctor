# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from django import forms
from django.http import HttpResponse
import ast


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest11632(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse('<script src="' + str(processed) + '"></script>', content_type='text/html')
