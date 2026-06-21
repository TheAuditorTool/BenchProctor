# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest44061(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ensure_str(origin_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
