# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27356(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
