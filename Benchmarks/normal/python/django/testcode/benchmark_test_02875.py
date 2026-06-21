# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02875(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
