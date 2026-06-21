# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def BenchmarkTest06977(request):
    multipart_value = request.POST.get('multipart_field', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(multipart_value))
    return JsonResponse({"saved": True})
