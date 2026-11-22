# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os
from app_runtime import db


def BenchmarkTest00068(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
