# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from django import forms
from types import SimpleNamespace


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest23350(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
