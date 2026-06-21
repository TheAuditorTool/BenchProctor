# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def BenchmarkTest77549(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
