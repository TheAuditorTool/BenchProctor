# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest48986(request):
    field_value = UserForm(request.POST).data.get('field', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(field_value),))
    return JsonResponse({'record': str(record)}, status=200)
