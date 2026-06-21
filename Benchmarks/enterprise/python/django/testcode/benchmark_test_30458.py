# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30458(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
