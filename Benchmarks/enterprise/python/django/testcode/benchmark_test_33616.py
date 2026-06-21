# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33616(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
