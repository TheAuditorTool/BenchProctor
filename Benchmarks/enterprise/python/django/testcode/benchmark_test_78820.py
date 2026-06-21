# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78820(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
