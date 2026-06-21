# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13322(request):
    cookie_value = request.COOKIES.get('session_token', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
