# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest34367(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
