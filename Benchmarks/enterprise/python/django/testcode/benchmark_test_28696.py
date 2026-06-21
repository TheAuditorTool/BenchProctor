# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os


def relay_value(value):
    return value

def BenchmarkTest28696(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = relay_value(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
