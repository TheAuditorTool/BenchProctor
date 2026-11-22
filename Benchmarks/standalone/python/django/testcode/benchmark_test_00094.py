# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00094(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header!s}'
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.#%\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
