# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json
import os


def BenchmarkTest00035(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return JsonResponse({"saved": True})
