# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json
import os


def BenchmarkTest00010(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return JsonResponse({"saved": True})
