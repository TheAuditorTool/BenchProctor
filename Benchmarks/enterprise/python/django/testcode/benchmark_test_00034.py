# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest00034(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
