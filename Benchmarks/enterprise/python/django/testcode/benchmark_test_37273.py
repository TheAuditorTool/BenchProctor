# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import asyncio
import runpy
from types import SimpleNamespace


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest37273(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
