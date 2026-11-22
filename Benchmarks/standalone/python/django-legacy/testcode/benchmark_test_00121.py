# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os


def BenchmarkTest00121(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(ua_value).strip()
        case _:
            data = str(ua_value)
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
