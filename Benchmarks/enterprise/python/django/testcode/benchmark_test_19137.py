# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest19137(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
