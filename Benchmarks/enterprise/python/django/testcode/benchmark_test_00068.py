# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest00068(request):
    user_id = request.GET.get('id', '')
    data = to_text(user_id)
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
