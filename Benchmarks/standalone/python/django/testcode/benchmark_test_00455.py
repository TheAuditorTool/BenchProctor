# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os
import re


def BenchmarkTest00455(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
