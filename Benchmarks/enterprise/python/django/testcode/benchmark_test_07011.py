# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07011(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    def _primary():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
