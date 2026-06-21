# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57596(request, path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
