# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08253(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
