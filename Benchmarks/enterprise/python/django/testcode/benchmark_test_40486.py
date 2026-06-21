# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40486(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
