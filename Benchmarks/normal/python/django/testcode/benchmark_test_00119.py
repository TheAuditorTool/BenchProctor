# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest00119(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = default_blank(origin_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
