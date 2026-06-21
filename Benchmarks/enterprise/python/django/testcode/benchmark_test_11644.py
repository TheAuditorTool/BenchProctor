# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest11644(request):
    field_value = UserForm(request.POST).data.get('field', '')
    subprocess.Popen('echo ' + str(field_value), shell=True).wait()
    return JsonResponse({"saved": True})
