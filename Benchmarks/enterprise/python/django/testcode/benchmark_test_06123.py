# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06123(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
