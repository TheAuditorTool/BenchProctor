# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os


def BenchmarkTest00159(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
