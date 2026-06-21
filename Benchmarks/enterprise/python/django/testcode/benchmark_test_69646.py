# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import re


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest69646(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
