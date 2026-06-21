# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47660(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = forwarded_ip
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
