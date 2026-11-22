# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os


def BenchmarkTest00046(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '{}'.format(header_value)
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
