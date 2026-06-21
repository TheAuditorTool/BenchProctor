# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03686(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(forwarded_ip)})
