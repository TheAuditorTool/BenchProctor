# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from urllib.parse import unquote
from django import forms
import subprocess


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest64374(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
