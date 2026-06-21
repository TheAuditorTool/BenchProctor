# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import pickle


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest69327(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = RequestPayload(field_value).value
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
