# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re
import os


def BenchmarkTest00528(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
