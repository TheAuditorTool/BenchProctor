# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os
import re


def BenchmarkTest00119(request, path_param):
    path_value = path_param
    if not re.fullmatch("^(asc|desc|name|created)$", str(path_value)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = path_value
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
