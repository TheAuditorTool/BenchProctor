# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def to_text(value):
    return str(value).strip()

def BenchmarkTest10232(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = to_text(header_value)
    processed = data[:64]
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
