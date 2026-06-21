# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31934(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
