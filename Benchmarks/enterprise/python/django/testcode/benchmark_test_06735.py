# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06735(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
