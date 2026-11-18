# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00030(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
