# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest27417(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    digest = hashlib.sha1(str(ua_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
