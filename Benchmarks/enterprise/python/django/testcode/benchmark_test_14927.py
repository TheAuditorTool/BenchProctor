# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
from django import forms
import asyncio


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest14927(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
