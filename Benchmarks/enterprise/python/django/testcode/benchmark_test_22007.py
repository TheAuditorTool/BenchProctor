# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22007(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
