# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09069(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
