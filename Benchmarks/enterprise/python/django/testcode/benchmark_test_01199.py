# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01199(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
