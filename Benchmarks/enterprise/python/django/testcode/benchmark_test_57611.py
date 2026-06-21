# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from types import SimpleNamespace


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest57611(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
