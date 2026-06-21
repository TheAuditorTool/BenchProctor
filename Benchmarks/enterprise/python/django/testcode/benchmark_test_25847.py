# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25847(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
