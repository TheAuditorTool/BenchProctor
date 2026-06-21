# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80599(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
