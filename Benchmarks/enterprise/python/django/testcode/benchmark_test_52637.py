# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52637(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
