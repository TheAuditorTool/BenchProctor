# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09520(request, path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
