# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os


def BenchmarkTest00190(request):
    raw_body = request.body.decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(raw_body).strip()
        case _:
            data = str(raw_body)
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return JsonResponse({"saved": True})
