# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05584(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
