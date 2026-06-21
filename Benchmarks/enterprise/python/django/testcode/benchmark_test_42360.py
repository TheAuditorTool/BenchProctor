# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42360(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
