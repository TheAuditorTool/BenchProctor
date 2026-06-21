# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77495(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
