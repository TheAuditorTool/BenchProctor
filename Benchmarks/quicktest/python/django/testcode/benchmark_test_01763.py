# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01763(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
