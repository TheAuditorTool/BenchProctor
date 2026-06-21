# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03408(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
