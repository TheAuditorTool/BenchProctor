# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms
from django.shortcuts import redirect
import urllib.parse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest44233(request):
    field_value = UserForm(request.POST).data.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
