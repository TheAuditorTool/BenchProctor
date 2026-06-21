# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest10243(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.seteuid(65534)
    return JsonResponse({"saved": True})
