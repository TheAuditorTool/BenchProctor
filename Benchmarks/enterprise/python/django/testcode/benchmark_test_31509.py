# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31509(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
