# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest71377(request, path_param):
    path_value = path_param
    data = handle(path_value)
    processed = data[:64]
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
