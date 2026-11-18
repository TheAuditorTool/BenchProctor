# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import json
import os
from marshmallow import Schema, fields, validate, ValidationError


def BenchmarkTest00393(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.#%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
