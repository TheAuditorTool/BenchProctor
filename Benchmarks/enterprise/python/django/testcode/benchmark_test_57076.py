# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django import forms
import asyncio


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def relay_value(value):
    return value

def BenchmarkTest57076(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = relay_value(field_value)
    async def _evasion_task():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return asyncio.run(_evasion_task())
