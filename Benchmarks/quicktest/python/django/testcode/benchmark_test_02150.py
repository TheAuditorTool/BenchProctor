# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02150(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
