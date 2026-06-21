# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33854(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
