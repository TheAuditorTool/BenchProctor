# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39578(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
