# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59526(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
