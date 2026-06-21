# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import re


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest27868(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
