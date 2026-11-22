# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os


def BenchmarkTest00136(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(auth_header) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
