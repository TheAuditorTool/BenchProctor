# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import jsonschema
import os


def BenchmarkTest00136(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value!s}'
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.#%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
