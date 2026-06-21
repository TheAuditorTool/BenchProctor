# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)
@dataclass
class FormData:
    payload: str

def BenchmarkTest72711(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = FormData(payload=field_value).payload
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
