# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16095(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
