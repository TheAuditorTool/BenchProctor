# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
import asyncio
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest39522(request):
    field_value = UserForm(request.POST).data.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    async def _evasion_task():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
