# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05749(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
