# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os
from marshmallow import Schema, fields, validate, ValidationError


def BenchmarkTest00042(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body!s}'
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.#%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.compare_s('uid=' + str(processed) + ',ou=people,dc=example,dc=com', 'employeeType', b'staff')
    return JsonResponse({"saved": True})
