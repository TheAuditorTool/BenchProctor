# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76267(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
