# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import os
from rest_framework import serializers


def BenchmarkTest00627(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    class _InputSerializer(serializers.Serializer):
        value = serializers.RegexField("^[a-zA-Z0-9 _.#%\\-]+$")
    _ser = _InputSerializer(data={'value': str(data)})
    if not _ser.is_valid():
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return JsonResponse({"saved": True})
