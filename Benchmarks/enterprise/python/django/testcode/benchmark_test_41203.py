# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41203(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
