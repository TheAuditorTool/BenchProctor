# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from django.shortcuts import redirect
import asyncio
import urllib.parse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest16063(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
