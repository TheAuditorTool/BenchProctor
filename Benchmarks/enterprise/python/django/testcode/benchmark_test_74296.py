# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74296(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
