# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django import forms
import re


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest12698(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
