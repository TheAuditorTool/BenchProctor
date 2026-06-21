# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
import subprocess


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest09920(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
