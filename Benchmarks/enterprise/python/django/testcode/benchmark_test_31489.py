# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from urllib.parse import unquote


def BenchmarkTest31489(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
