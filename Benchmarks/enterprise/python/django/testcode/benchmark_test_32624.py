# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32624(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
