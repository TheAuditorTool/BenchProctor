# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def coalesce_blank(value):
    return value or ''

def BenchmarkTest60175(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = coalesce_blank(auth_header)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
