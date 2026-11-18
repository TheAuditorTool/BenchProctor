# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os


def BenchmarkTest00092(request):
    field_value = request.POST.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return JsonResponse({"saved": True})
