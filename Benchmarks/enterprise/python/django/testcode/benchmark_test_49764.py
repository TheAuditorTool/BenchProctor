# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49764(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
