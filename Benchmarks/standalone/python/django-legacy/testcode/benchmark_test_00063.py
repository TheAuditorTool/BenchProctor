# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from rest_framework import serializers


def BenchmarkTest00063(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    class _InputSerializer(serializers.Serializer):
        value = serializers.RegexField("^[a-zA-Z0-9 _.%\\-]+$")
    _ser = _InputSerializer(data={'value': str(data)})
    if not _ser.is_valid():
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
