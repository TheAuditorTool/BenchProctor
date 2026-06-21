# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75572(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
