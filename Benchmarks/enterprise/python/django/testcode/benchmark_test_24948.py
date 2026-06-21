# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json
import asyncio
from types import SimpleNamespace


def BenchmarkTest24948(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
