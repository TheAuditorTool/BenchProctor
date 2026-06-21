# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70823(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
