# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from urllib.parse import unquote
import os
import re


def BenchmarkTest00711(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
