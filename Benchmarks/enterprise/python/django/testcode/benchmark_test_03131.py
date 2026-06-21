# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03131(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
