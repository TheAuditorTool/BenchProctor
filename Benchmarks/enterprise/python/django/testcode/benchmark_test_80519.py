# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80519(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
