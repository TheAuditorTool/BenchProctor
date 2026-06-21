# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44883(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
