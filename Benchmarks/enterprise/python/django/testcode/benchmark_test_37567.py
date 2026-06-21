# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37567(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
