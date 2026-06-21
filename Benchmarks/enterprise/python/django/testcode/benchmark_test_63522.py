# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63522(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
