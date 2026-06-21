# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from django import forms
import time
import asyncio


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest40512(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
