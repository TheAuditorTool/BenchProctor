# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22239(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % str(forwarded_ip)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
