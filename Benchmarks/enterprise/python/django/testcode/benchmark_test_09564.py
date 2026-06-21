# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09564(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
