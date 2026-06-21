# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40657(request):
    host_value = request.META.get('HTTP_HOST', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
