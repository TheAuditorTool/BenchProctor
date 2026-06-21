# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22019(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
