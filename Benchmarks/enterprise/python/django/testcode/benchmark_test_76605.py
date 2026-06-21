# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest76605(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
