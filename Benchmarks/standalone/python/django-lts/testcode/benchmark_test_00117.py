# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os


def BenchmarkTest00117(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
