# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import re
import os


def BenchmarkTest00128(request):
    field_value = request.POST.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(field_value).strip()
        case _:
            data = str(field_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
