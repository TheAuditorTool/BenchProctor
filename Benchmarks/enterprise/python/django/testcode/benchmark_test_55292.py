# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55292(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % str(forwarded_ip)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
