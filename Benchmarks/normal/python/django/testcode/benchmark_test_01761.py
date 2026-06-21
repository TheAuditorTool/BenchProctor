# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01761(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
