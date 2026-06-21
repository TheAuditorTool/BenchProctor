# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12312(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
