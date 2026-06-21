# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67652(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
