# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25808(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
