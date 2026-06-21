# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from types import SimpleNamespace
from lxml import etree


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest29853(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
