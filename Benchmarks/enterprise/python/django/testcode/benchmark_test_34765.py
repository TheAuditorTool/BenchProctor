# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34765(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
