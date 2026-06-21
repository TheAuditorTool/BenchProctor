# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12986(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
