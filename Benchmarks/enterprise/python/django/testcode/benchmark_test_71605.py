# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71605(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
