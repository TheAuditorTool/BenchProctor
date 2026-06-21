# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import requests


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07147(request):
    field_value = UserForm(request.POST).data.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
