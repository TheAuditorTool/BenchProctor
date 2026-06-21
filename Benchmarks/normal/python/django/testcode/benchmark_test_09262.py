# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09262(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
