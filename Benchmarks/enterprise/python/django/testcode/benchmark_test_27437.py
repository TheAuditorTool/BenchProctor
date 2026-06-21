# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27437(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
