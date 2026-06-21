# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from types import SimpleNamespace


def BenchmarkTest16286(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    def _primary():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
