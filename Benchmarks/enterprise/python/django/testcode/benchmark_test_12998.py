# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12998(request, path_param):
    path_value = path_param
    return JsonResponse({'error': str(path_value), 'stack': repr(locals())}, status=500)
