# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26209(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
