# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest62494(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
