# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import asyncio
from types import SimpleNamespace


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest35079(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
