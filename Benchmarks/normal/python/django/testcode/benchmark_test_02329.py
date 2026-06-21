# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02329(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    async def _evasion_task():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
