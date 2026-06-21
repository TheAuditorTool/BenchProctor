# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34537(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
