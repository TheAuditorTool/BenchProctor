# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import json
import os


def BenchmarkTest00214(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
