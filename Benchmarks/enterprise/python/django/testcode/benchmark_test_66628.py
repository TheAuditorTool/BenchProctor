# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66628(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
