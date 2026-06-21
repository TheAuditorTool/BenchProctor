# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


def BenchmarkTest59397(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = header_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
