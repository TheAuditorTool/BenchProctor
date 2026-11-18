# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re
import json
import os


def BenchmarkTest00017(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
