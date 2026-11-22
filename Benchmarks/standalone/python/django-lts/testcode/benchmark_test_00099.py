# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re
import os


def BenchmarkTest00099(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.compare_s('uid=' + str(processed) + ',ou=people,dc=example,dc=com', 'employeeType', b'staff')
    return JsonResponse({"saved": True})
