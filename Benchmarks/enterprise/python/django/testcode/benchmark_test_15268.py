# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15268(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
