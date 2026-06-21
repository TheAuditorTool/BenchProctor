# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01197(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
