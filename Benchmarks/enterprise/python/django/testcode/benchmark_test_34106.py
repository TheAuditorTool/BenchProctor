# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34106(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
