# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json
import os
import re


def BenchmarkTest00005(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
