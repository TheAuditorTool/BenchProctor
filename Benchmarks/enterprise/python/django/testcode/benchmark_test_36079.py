# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36079(request, path_param):
    path_value = path_param
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
