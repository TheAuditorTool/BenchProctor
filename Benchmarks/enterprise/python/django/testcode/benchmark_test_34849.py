# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34849(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
