# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69060(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
