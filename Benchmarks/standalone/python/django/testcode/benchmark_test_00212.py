# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import re
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00212(request):
    xml_value = request.body.decode('utf-8')
    form = FormData(payload=xml_value)
    data = form.payload
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
