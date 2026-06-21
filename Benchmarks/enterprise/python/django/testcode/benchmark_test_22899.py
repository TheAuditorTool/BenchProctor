# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


def ensure_str(value):
    return str(value)

def BenchmarkTest22899(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ensure_str(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
