# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest41871(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    digest = hashlib.md5(str(origin_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
