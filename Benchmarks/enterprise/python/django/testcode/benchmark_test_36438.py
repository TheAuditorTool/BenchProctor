# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from django import forms
import subprocess


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest36438(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
