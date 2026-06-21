# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def coalesce_blank(value):
    return value or ''

def BenchmarkTest04675(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = coalesce_blank(field_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
