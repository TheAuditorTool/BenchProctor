# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def to_text(value):
    return str(value).strip()

def BenchmarkTest68138(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = to_text(field_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
