# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30827(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
