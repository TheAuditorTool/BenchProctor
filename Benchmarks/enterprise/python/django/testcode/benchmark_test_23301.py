# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def ensure_str(value):
    return str(value)

def BenchmarkTest23301(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ensure_str(field_value)
    processed = data[:64]
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return JsonResponse({'record': str(record)}, status=200)
