# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def BenchmarkTest04492(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
