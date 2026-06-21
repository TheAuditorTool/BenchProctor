# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05885(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = default_blank(multipart_value)
    eval(compile("conn = ldap.initialize('ldap://localhost:389')\nconn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
