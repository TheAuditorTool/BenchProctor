# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import jsonschema
import os


def BenchmarkTest00123(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.#%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
