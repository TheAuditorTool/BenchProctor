# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re
import os


def BenchmarkTest07266(request):
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = env_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
