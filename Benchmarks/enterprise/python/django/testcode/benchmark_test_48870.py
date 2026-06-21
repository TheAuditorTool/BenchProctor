# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48870(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
