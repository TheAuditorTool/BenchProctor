# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest24662(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
