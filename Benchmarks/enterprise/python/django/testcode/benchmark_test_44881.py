# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest44881(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = coalesce_blank(origin_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
