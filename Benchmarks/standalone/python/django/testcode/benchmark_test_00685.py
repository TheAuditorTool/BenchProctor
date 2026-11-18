# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00685(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
