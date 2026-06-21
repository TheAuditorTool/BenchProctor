# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19803(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
