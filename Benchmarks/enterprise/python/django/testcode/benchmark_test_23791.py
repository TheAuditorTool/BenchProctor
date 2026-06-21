# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23791(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
