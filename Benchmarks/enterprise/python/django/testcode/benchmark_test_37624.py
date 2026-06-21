# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import re


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest37624(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = field_value
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
