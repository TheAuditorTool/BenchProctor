# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10000(request):
    field_value = UserForm(request.POST).data.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
