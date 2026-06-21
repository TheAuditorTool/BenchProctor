# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest49931(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    digest = hashlib.sha256(str(referer_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
