# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00065(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ' '.join(parts)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
