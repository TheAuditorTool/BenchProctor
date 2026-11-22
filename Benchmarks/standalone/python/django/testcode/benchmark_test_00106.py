# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json
import os
from pydantic import Field, ValidationError, create_model


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00106(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = RequestPayload(json_value).value
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.#%\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.compare_s('uid=' + str(processed) + ',ou=people,dc=example,dc=com', 'employeeType', b'staff')
    return JsonResponse({"saved": True})
