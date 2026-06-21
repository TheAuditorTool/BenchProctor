# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from django import forms
import asyncio


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest56295(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
