# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14040(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
