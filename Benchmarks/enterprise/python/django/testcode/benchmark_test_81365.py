# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest81365(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', field_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = field_value
    eval(str(processed))
    return JsonResponse({"saved": True})
