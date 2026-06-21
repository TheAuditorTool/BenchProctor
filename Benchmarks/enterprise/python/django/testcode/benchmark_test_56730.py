# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56730(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
