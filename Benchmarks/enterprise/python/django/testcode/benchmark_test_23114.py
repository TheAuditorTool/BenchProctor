# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from django import forms
import asyncio


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest23114(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
