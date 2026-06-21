# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest06159(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
