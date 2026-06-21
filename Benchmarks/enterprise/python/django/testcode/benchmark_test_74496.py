# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from django import forms
import asyncio
import subprocess


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest74496(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
