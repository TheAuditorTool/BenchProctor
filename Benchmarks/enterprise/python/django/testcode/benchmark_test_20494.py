# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20494(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
