# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


def BenchmarkTest11351(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
