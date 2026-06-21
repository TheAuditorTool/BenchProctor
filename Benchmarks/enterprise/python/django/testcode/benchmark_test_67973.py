# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest67973(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = RequestPayload(field_value).value
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
