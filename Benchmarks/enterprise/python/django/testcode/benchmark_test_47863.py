# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest47863(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = (lambda v: v.strip())(field_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
