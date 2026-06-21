# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json


def BenchmarkTest65341(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = json_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
