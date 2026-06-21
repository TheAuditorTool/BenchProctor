# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
import subprocess


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest07734(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
