# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40042(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
