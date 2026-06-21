# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44106(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
