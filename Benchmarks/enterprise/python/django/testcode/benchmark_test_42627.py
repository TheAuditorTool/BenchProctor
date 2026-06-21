# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42627(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
