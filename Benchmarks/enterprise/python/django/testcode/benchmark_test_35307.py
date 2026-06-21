# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest35307(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    digest = str(ua_value).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
