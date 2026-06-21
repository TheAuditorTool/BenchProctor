# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def normalise_input(value):
    return value.strip()

def BenchmarkTest47760(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = normalise_input(field_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['user'] = str(processed)
    return JsonResponse({"saved": True})
