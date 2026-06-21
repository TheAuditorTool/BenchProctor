# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50612(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    match str(header_value):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
