# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json


def BenchmarkTest59534(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
