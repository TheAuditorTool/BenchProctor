# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12521(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
