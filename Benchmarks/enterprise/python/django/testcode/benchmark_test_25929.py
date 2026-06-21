# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25929(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
