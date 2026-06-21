# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest41336(request):
    field_value = UserForm(request.POST).data.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
