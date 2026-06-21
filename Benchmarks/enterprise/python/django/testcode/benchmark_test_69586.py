# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69586(request, path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
