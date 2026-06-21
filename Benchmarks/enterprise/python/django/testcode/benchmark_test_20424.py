# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20424(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
