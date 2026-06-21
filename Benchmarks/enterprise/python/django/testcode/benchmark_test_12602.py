# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def BenchmarkTest12602(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
