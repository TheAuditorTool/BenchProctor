# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36211(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
