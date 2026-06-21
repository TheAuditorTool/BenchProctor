# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest06084(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = RequestPayload(field_value).value
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
