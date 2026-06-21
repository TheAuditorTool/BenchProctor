# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17778(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = forwarded_ip if forwarded_ip else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
