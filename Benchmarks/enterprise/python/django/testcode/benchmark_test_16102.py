# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)
@dataclass
class FormData:
    payload: str

def BenchmarkTest16102(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = FormData(payload=field_value).payload
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
