# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01832(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
