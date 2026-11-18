# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os


def BenchmarkTest00715(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return JsonResponse({"saved": True})
