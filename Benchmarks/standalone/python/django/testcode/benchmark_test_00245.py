# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00245(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
