# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest29237(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
