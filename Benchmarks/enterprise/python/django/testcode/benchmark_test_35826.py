# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest35826(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return JsonResponse({"saved": True})
