# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os
from app_runtime import db


def BenchmarkTest00047(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(data) + ')')
    return JsonResponse({"saved": True})
