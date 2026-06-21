# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17958(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
