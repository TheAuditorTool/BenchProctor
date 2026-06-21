# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29719(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
