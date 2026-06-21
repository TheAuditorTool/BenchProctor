# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from urllib.parse import unquote


def BenchmarkTest61860(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
