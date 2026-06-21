# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32237(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
