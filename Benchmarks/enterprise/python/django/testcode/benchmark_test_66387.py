# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
import subprocess


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest66387(request):
    field_value = UserForm(request.POST).data.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
