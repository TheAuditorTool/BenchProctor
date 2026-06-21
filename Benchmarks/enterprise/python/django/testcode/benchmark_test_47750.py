# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47750(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
