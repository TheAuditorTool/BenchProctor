# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest00590(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = RequestPayload(field_value).value
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
