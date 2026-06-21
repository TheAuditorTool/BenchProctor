# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest57372(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    if not re.fullmatch('^[\\w\\s.*]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
