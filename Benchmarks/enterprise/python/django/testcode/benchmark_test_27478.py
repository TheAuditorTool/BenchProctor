# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27478(request):
    multipart_value = request.POST.get('multipart_field', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
