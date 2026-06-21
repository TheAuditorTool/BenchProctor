# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77804(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
