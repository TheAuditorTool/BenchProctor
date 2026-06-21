# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75961(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
