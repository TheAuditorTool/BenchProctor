# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest61922(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
