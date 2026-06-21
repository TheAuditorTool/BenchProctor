# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest72518(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
