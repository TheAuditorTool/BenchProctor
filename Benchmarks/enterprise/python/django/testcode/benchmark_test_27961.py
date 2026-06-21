# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27961(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
