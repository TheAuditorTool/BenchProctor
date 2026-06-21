# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17343(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
