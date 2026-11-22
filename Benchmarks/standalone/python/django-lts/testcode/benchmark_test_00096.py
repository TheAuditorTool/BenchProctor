# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache
import re


def BenchmarkTest00096(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if not re.fullmatch("^(asc|desc|name|created)$", str(auth_header)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = auth_header
    cache.set('active_tenant', str(processed), None)
    return JsonResponse({"saved": True})
