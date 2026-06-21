# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10723(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
