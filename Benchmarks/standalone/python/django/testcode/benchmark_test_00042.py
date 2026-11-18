# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from rest_framework import serializers


def BenchmarkTest00042(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    class _InputSerializer(serializers.Serializer):
        value = serializers.RegexField("^[a-zA-Z0-9 _.\\-]+$")
    _ser = _InputSerializer(data={'value': str(data)})
    if not _ser.is_valid():
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
