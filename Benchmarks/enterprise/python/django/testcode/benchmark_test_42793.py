# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest42793(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    digest = hashlib.sha256(('static_salt_123' + str(ua_value)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
