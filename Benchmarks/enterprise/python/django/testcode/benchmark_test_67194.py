# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest67194(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
