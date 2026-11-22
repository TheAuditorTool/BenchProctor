# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00039(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = RequestPayload(auth_header).value
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
