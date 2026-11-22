# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00149(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    digest = hashlib.sha3_256(str(ua_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
