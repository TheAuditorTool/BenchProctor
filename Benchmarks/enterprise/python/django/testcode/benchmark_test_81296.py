# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest81296(request):
    field_value = UserForm(request.POST).data.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
