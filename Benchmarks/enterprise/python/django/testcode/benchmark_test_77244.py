# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re
import json
from types import SimpleNamespace


def BenchmarkTest77244(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.*]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
