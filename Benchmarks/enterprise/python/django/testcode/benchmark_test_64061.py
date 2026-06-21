# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64061(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
