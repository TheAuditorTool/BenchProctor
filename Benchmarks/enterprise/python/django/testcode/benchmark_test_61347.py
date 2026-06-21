# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61347(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
