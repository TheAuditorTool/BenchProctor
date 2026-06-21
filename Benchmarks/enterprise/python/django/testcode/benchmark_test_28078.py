# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28078(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
