# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest32436(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = FormData(payload=auth_header).payload
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
