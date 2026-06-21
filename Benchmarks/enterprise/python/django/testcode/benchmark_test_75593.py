# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75593(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
