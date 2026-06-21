# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


def BenchmarkTest54885(request):
    xml_value = request.body.decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(xml_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = xml_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
