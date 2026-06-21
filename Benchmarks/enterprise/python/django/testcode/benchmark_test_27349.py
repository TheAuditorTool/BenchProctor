# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27349(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
