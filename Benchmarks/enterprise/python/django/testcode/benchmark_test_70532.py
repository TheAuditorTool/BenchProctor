# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import re


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest70532(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if re.search('[a-zA-Z0-9_-]+', str(field_value)):
        return JsonResponse({'validated': str(field_value)}, status=200)
    return JsonResponse({"saved": True})
