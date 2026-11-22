# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os
from marshmallow import Schema, fields, validate, ValidationError


def BenchmarkTest00031(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.#%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
