# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35019(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
