# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


def BenchmarkTest52662(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
