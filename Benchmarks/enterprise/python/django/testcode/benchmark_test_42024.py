# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def normalise_input(value):
    return value.strip()

def BenchmarkTest42024(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    eval(compile("conn = ldap.initialize('ldap://localhost:389')\nconn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
