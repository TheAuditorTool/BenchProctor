# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap3
import os
from rest_framework import serializers


def BenchmarkTest00119(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % (env_value,)
    class _InputSerializer(serializers.Serializer):
        value = serializers.RegexField("^[a-zA-Z0-9 _.#%\\-]+$")
    _ser = _InputSerializer(data={'value': str(data)})
    if not _ser.is_valid():
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return JsonResponse({"saved": True})
