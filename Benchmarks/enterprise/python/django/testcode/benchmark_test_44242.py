# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest44242(request):
    field_value = UserForm(request.POST).data.get('field', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(field_value))
    return JsonResponse({"saved": True})
