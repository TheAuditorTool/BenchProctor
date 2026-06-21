# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04145(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
