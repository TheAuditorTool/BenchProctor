# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12712(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
