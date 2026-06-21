# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest06628(request, path_param):
    path_value = path_param
    data = relay_value(path_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
