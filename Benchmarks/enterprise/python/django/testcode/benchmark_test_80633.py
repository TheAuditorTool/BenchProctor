# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80633(request, path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
