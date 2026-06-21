# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72560(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
