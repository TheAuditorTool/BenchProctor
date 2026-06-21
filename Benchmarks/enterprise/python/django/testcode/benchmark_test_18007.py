# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18007(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
