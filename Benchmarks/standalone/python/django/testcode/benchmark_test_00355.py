# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00355(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return JsonResponse({"saved": True})
