# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50684(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
