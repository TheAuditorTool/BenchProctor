# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
import asyncio


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def relay_value(value):
    return value

def BenchmarkTest18424(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = relay_value(field_value)
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
