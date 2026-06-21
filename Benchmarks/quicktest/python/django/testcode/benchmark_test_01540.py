# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


def relay_value(value):
    return value

def BenchmarkTest01540(request):
    xml_value = request.body.decode('utf-8')
    data = relay_value(xml_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
