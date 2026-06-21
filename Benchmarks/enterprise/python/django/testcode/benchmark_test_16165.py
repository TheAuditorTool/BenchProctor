# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16165(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
