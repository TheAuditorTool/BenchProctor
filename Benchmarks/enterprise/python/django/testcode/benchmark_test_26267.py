# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from django import forms
from types import SimpleNamespace


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest26267(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
