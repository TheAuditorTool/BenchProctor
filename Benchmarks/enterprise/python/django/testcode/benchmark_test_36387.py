# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from django import forms
import json


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest36387(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
