# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest30131(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = f'{field_value:.200s}'
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
