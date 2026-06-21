# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04960(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
