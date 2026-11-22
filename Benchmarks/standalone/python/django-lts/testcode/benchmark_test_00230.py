# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import json
import os
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00230(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.#%\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
