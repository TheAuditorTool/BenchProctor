# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest23623(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
