# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65735(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    return JsonResponse({'error': str(origin_value), 'stack': repr(locals())}, status=500)
