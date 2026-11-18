# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from urllib.parse import unquote
import os
from marshmallow import Schema, fields, validate, ValidationError


def BenchmarkTest00399(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.#%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
