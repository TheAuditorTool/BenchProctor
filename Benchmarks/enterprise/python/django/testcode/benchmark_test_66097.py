# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66097(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
