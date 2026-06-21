# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from app_runtime import db


def BenchmarkTest01097(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
