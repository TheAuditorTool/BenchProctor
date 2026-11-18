# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re
import os


def BenchmarkTest00490(request):
    user_id = request.GET.get('id', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", user_id):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = user_id
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
