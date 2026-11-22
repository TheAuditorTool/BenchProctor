# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os


def BenchmarkTest00042(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.compare_s('uid=' + str(data) + ',ou=people,dc=example,dc=com', 'employeeType', b'staff')
    return JsonResponse({"saved": True})
