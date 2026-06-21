# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47272(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
