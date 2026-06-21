# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39440(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
