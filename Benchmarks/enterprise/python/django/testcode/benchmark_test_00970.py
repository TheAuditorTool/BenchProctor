# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest00970(request):
    field_value = UserForm(request.POST).data.get('field', '')
    subprocess.run(['echo', field_value], shell=False)
    return JsonResponse({"saved": True})
