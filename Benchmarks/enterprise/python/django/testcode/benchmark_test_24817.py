# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from django import forms
import asyncio


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest24817(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
