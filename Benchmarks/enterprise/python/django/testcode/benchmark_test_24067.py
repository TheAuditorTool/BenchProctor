# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
from django.http import HttpResponse
import ast
import asyncio


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest24067(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    async def _evasion_task():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return asyncio.run(_evasion_task())
