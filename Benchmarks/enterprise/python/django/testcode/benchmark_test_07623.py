# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest07623(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
