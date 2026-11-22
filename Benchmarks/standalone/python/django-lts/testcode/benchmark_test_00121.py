# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00121(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.compare_s('uid=' + str(data) + ',ou=people,dc=example,dc=com', 'employeeType', b'staff')
    return JsonResponse({"saved": True})
