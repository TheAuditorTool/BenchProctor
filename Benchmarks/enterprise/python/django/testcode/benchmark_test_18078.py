# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18078(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
