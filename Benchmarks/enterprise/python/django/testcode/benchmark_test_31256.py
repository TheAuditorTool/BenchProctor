# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from types import SimpleNamespace


def BenchmarkTest31256(request):
    user_id = request.GET.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
