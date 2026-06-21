# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64844(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
