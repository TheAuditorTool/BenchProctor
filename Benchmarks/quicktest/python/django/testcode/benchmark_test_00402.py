# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from lxml import etree


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest00402(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
