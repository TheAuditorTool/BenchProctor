# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def BenchmarkTest37645(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
