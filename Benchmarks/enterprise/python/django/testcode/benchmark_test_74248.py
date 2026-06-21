# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest74248(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
