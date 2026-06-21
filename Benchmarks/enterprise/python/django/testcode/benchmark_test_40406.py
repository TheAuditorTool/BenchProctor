# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40406(request, path_param):
    path_value = path_param
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(path_value)})
