# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12380(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
