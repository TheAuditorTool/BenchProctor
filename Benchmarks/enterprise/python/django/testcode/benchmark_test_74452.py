# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from lxml import etree


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest74452(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = RequestPayload(field_value).value
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
