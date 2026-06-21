# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02677(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
