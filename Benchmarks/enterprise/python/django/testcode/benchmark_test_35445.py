# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35445(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
