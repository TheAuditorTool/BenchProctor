# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def coalesce_blank(value):
    return value or ''

def BenchmarkTest81337(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
