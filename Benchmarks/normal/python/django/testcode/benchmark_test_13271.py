# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from django import forms
from types import SimpleNamespace


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest13271(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
