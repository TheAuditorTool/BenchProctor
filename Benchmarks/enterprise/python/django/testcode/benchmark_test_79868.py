# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import asyncio
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest79868(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    if data != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
