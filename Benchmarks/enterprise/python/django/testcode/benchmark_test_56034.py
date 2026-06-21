# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56034(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
