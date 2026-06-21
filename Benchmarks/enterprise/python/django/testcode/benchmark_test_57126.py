# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57126(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
