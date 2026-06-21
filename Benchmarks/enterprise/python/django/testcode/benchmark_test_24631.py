# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest24631(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
