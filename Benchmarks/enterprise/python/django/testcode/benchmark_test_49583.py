# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49583(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
