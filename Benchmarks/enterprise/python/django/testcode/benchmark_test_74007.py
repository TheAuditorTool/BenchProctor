# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
@dataclass
class FormData:
    payload: str

def BenchmarkTest74007(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = FormData(payload=field_value).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
