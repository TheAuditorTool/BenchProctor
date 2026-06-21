# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from django import forms
import time


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def to_text(value):
    return str(value).strip()

def BenchmarkTest08654(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = to_text(field_value)
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
