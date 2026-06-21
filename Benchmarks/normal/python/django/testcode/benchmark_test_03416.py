# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03416(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
