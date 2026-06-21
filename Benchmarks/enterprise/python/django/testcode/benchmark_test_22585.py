# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22585(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
