# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03282(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
