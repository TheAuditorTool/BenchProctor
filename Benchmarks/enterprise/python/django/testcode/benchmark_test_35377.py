# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35377(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
