# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59614(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
