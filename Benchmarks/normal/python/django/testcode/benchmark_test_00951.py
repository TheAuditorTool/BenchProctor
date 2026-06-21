# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00951(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.*]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
