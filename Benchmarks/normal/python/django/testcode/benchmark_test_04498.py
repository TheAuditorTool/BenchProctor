# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
@dataclass
class FormData:
    payload: str

def BenchmarkTest04498(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = FormData(payload=field_value).payload
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
